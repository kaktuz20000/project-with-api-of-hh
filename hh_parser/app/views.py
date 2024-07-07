from flask import request, jsonify
from app import app, db
from app.models import Candidate, Vacancy
from app.utils import fetch_candidates, fetch_vacancies

@app.route('/parse_candidates', methods=['GET'])
def parse_candidates():
    params = request.args.to_dict()
    candidates = fetch_candidates(params)
    for candidate_data in candidates:
        candidate = Candidate(**candidate_data)
        db.session.add(candidate)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Candiates parsed and stored successfuly'})

@app.route('/parse_vacancies', methods=['GET'])
def parse_vacancies():
    params = request.args.to_dict()
    vacancies = fetch_vacancies(params)
    for vacancy_data in vacancies:
        vacancy = Vacancy(**vacancy_data)
        db.session.add(vacancy)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Vacancies parsed and stodre successfully'})

@app.route('/analytics', methods=['GET'])
def analytics():
    vacancies_count = Vacancy.query.count()
    candidates_count = Candidate.query.count()
    return jsonify({'vacancies_count': vacancies_count, 'candidates_count': candidates_count})