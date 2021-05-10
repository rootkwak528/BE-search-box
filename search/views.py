from django.shortcuts import render
from django.http import JsonResponse
from decouple import config
import requests
import pprint


API_URL = 'https://api.themoviedb.org/3'
API_KEY = config('API_KEY')


def search_tmdb(request):
    return render(request, 'search/search.html')


def get_url(category='movie', feature='', **kwargs):
    url = f'{API_URL}/{category}/{feature}'
    url += f'?api_key={API_KEY}'

    for k, v in kwargs.items():
        url += f'&{k}={v}'
    return url


def get_movie_data(request, title='dark knight'):
    url = get_url('search', 'movie', region='KR', language='ko', query=request.GET.get('title'))
    res = requests.get(url)

    movie = res.json()
    movie_data = {'data': movie.get('results')}
    pprint.pprint(movie_data)
    return JsonResponse(movie_data)