from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import get_object_or_404, render
from . import views
def index(request):
    return render(request, 'locationgameapp/index.html')

def signUp(request):
    return render(request, 'locationgameapp/signUp.html')

#def login(request):
    #return render(request, 'locationgameapp/login.html')

@login_required
def homePage(request):
    return render(request,'locationgameapp/homePage.html')

@login_required
def Game(request):
    return render(request,'locationgameapp/game.html')

@login_required
def Settings(request):
    return render(request, 'locationgameapp/settings.html')

@login_required
def Leaderboards(request):
    return render(request, 'locationgameapp/Leaderboards.html')

