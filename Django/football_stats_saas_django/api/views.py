from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.


def match_data(request):
    headers = {'X-RapidAPI-Key': 'your_api_key'}
    response = requests.get('https://api.rapidapi.com/soccer/', headers=headers)
    return JsonResponse(response.json())
    #return JsonResponse({'message': 'Match data endpoint'})