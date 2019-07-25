from django.shortcuts import render

def index(request):
    name = {'first': 'Jane', 'family': 'Smith'}
    return render(request, "greet/index.html", name)
