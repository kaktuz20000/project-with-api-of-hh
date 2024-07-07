from django.shortcuts import render
from django.http import JsonResponse
import requests

FLASK_BACKEND_URL = 'http://web:5000'

def index(request):
    return render(request, 'index.html')

def parse(request):
    entity_type = request.GET.get('entity_type')
    params = request.GET.dict()
    
    if entity_type == 'candidates':
        response = requests.get(f'{FLASK_BACKEND_URL}/parse_candidates', params=params)
    elif entity_type == 'vacancies':
        response = requests.get(f'{FLASK_BACKEND_URL}/parse_vacancies', params=params)
    
    return JsonResponse(response.json())

def analytics(request):
    response = requests.get(f'{FLASK_BACKEND_URL}/analytics')
    return JsonResponse(response.json())