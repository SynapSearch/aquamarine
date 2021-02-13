from django.shortcuts import render, redirect
from ..models import UserProfile, RecruiterProfile, StudentProfile
from ..forms import UserSignupForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
	return render(request, 'home.html')

@login_required
def browse(request):
    return render(request, 'browse.html')

def signup(request, *args, **kargs):
    if request.user.is_authenticated:
        return redirect('browse')

    if request.method == 'POST':
        if 'signupbutton' in request.POST:
            form = UserSignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                if user.is_recruiter:
                    profile = RecruiterProfile.objects.create(user=user)
                else:
                    profile = StudentProfile.objects.create(user=user)
                user.save(commit=True)
                profile.save()
                login(request, user)
                return redirect('browse')
        elif 'loginbutton' in request.POST:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('browse')
    else:
        form = UserSignupForm()


    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
	return redirect('home')
