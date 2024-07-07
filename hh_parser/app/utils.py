import requests

def fetch_candidates(params):
    response = requests.get('https://api.hh.ru/resumes', params=params)
    if response.status_code == 200:
        return response.json().get('items', [])
    return []

def fetch_vacancies(params):
    response = requests.get('https://api.hh.ru/vacancies', params=params)
    if response.status_code == 200:
        return response.json().get('items', [])
    return []