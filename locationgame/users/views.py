from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import views
from .forms import UserRegisterFrom

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created {username}!')
            return redirect('locationgameapp:homePage')
    else:
        form = UserRegisterFrom()
    return render(request, 'users/signUp.html', {'form': form})
