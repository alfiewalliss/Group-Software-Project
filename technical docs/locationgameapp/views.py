from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import task, pleaderboard
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .forms import profileUpdateForm, userUpdateForm

import json 

def index(request):
    return render(request, 'locationgameapp/index.html')

def signUp(request):
    return render(request, 'locationgameapp/signUp.html')

@login_required
def Game(request):
    taskList = list(task.objects.order_by('taskName').values())
    taskJson = json.dumps(taskList)
    top = pleaderboard.objects.all().order_by('-score')[:10]
    context = {'tasks': taskJson,
               'top_easy': top}

    if request.method == 'POST':
        if request.POST.get('SubmitScore'):
            try:
                plb = pleaderboard.objects.get(profile=request.user.profile)
                if plb != None:
                    old_score = plb.score
                    print(old_score)
                    new_score = request.POST.get('SubmitScore')
                    print(new_score)
                    if int(old_score) < int(new_score):
                        plb.score = new_score
                        plb.save()
            except:
                lb_obj = pleaderboard(
                    profile=request.user.profile,
                    score=request.POST.get('SubmitScore')
                )
                lb_obj.save()

    return render(request, 'locationgameapp/game.html', context)

@login_required
def Leaderboards(request):
    return render(request, 'locationgameapp/Leaderboards.html')

@login_required
def AddAdmin(request):
    if request.method == 'POST':
        if request.POST.get('AddSuperuser'):
            user1 = User.objects.get(username=request.POST.get('AddSuperuser'))
            user1.is_superuser = not user1.is_superuser
            user1.is_staff = not user1.is_staff
            user1.save()
        else:
            messages.warning(request, f'Error incorect format for user permissions')
    userList = User.objects.values()
    userDict = {'User': userList}
    return render(request, 'locationgameapp/addAdmin.html', userDict)

@login_required
def AddLocations(request):
    if request.method == 'POST':
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

        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            return redirect(reverse('UpdateProfile'))
    else:
        uform = userUpdateForm(instance=request.user)
        try:
            pform = profileUpdateForm(instance=request.user.profile)
        except:
            pform = {}

    context = {
        'uform' : uform,
        'pform' : pform
    }
    return render(request, 'locationgameapp/UpdateProfile.html', context)

    


