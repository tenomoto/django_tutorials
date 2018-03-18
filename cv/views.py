from django.shortcuts import render

from .models import Entry

def index(request):
    affiliation_list =  Entry.objects.order_by('date_join')
    return render(request, 'cv/index.html', {'affiliation_list': affiliation_list})