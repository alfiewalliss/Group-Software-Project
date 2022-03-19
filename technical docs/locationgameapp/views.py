from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import task
from .forms import UserCreationForm, profileUpdateForm, userUpdateForm

import json 

def index(request):
    return render(request, 'locationgameapp/index.html')

def signUp(request):
    return render(request, 'locationgameapp/signUp.html')

@login_required
def Game(request):
    taskList = list(task.objects.order_by('taskName').values()) 
    taskJson = json.dumps(taskList)  
    context = {'tasks': taskJson} 
    return render(request, 'locationgameapp/game.html', context) 

@login_required
def Leaderboards(request):
    return render(request, 'locationgameapp/Leaderboards.html')

@login_required
def AddLocations(request):
    if request.method == 'POST':
        print("hello")
        print(request.POST.get)
        task1 = task()
        task1.taskName = request.POST.get('Name' '')
        task1.description = request.POST.get('Name' '')
        task1.longitude = request.POST.get('Longitude' '')
        task1.latitude = request.POST.get('Latitude' '')
        task1.save()
    taskList = list(task.objects.order_by('taskName').values()) 
    taskJson = json.dumps(taskList)  
    context = {'tasks': taskJson} 
    return render(request, 'locationgameapp/addLocations.html', context) 

@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        uform = userUpdateForm(request.POST, instance=request.user)
        pform = profileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    else:
        uform = userUpdateForm(instance=request.user)
        pform = profileUpdateForm(instance=request.user.profile)

    context = {
        'uform' : uform,
        'pform' : pform
    }
    return render(request, 'locationgameapp/UpdateProfile.html', context)

    


