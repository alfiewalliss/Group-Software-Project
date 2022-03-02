'''Each page in the project'''
import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import task

def index(request):
    '''Rendering of the index page'''

    return render(request, 'locationgameapp/index.html')

def signUp(request):
    '''Rendering of the signUp page'''

    return render(request, 'locationgameapp/signUp.html')

@login_required
def Game(request):
    '''Rendering of the game page
    Additionally loads the data from the tasks table
    This is then used in the game.html js code'''

    #Sort by taskName
    taskList = list(task.objects.order_by('taskName').values())
    #Json file preparation
    taskJson = json.dumps(taskList)
    context = {'tasks': taskJson}
    return render(request, 'locationgameapp/game.html', context)

@login_required
def Leaderboards(request):
    '''Rendering of the Leaderboards page'''
    return render(request, 'locationgameapp/Leaderboards.html')
