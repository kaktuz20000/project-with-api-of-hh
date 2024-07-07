from app import db

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150))
    desired_position = db.Column(db.String(150))
    skills = db.Column(db.Text)
    work_format = db.Column(db.String(50))
    additional_info = db.Column(db.JSON)

class Vacancy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position_title = db.Column(db.String(150))
    required_skills = db.Column(db.Text)
    work_format = db.Column(db.String(50))
    additional_info = db.Column(db.JSON)