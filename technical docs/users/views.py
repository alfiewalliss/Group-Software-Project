'''Users views'''
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterFrom

# Create your views here.
#SignUp data handling
def register(request):
    if request.method == 'POST':
        #Recieve user input data
        form = UserRegisterFrom(request.POST)
        #If the form inputs are correct
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'users/signUp.html', {'form': form})
