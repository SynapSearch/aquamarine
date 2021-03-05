from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from django.urls import reverse

from ..models import UserProfile
from ..forms import UserSignupForm, UserLoginForm

def signup(request, *args, **kargs):
    if request.user.is_authenticated:
        if request.user.is_recruiter:
            return redirect('r_viewprofile')
        return redirect('browse', 0)

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.user.is_recruiter:
                return redirect('r_createprofile') 
            return redirect('s_createprofile')
    else:
        form = UserSignupForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request, *args, **kargs):
    if request.user.is_authenticated:
        if request.user.is_recruiter:
            return redirect('r_viewprofile')
        return redirect('browse', 0)

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.is_recruiter:
                return redirect('r_viewprofile')
            return redirect('browse', 0)
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
	return redirect('home')
