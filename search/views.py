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

    movies = {}
    for idx, movie in enumerate(res.json().get('results')[:10]):
        # pprint(movie)
        poster_id = movie.get('poster_path')
        movies[idx] = {
            'title': movie.get('title'),
            'poster_path': f'https://www.themoviedb.org/t/p/w92{poster_id}'
        }
    return JsonResponse(movies)