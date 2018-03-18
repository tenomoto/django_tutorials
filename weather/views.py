from django.shortcuts import render
from .weather import get_loc, get_forecast

def index(request):
    loc = get_loc()
    return render(request, 'weather/index.html', {'loc': loc})

def detail(request, loc):
    content = get_forecast(loc)
    return render(request, 'weather/detail.html', content)