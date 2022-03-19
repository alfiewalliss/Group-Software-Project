from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import task
from django.contrib import messages
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
        print(request.POST.get('LocationName'))
        if request.POST.get('Name') and request.POST.get('Longitude') and request.POST.get('Latitude'):
            name = request.POST.get('Name')
            try:
                longitude = float(request.POST.get('Longitude'))
                latitude = float(request.POST.get('Latitude'))
                if type(name) == str and type(longitude) == float and type(latitude) == float:
                    task1 = task()
                    task1.description = request.POST.get('Name')
                    task1.longitude = request.POST.get('Longitude')
                    task1.latitude = request.POST.get('Latitude')
                    task1.save()
                else:
                    messages.warning(request, f'Error incorect format for new task')
            except:
                messages.warning(request, f'Error incorect format for new task')  
        elif request.POST.get("LocationName"):
            task.objects.filter(description=request.POST.get("LocationName")).delete()
        else:
            messages.warning(request, f'Error incorect format for new task')
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

    


