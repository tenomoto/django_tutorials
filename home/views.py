from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "home/index.html")
    
@login_required
def memberonly(request):
    return render(request, "home/memberonly.html")