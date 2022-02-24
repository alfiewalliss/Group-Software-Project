from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request, 'locationgameapp/index.html')

def signUp(request):
    return render(request, 'locationgameapp/signUp.html')

def login(request):
    return render(request, 'locationgameapp/login.html')

def homePage(request):
    return render(request,'locationgameapp/homePage.html')

def Game(request):
    return render(request,'locationgameapp/game.html')

def Settings(request):
    return render(request, 'locationgameapp/settings.html')

def Leaderboards(request):
    return render(request, 'locationgameapp/Leaderboards.html')

