from django.shortcuts import render, redirect
from ..models import UserProfile, RecruiterProfile
from ..forms import UserSignupForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def browse(request):
    return render(request, 'browse.html')

def home(request):
    return render(request, 'home.html')

def signup(request, *args, **kargs):
    if request.user.is_authenticated:
        return redirect('browse')

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.user.is_recruiter:
                return redirect('r_createprofile')
            else: 
                return redirect('s_createprofile')
    else:
        form = UserSignupForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request, *args, **kargs):
    if request.user.is_authenticated:
        return redirect('browse')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('browse')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
	return redirect('home')
