from django.shortcuts import render


def search_tmdb(request):
    return render(request, 'search/search.html')