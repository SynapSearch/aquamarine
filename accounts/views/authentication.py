from django.shortcuts import render, redirect

from ..models import UserProfile, RecruiterProfile, StudentProfile, Experience, Project
from ..forms import UserSignupForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from jobs.models import Job


@login_required
def browse(request):
    ## replace with actual function that has a mathing alg 
    job = Job.objects.filter().first()
    context = {'job': job}

    return render(request, 'browse.html', context)

def r_browse(request, pk):
    ## replace with actual helper function that has a mathing alg 
    student = StudentProfile.objects.first()
    exp = Experience.objects.filter(created_by=student.user)
    project = Project.objects.filter(created_by=student.user)
    context = {'student': student, 'exp': exp, 'project': project}
    
    return render(request, 'browse.html', context)

def home(request):
    if request.user.is_authenticated:
        if request.user.is_recruiter:
            return redirect('r_viewprofile')
        return redirect('browse')

    return render(request, 'home.html')

def signup(request, *args, **kargs):
    if request.user.is_authenticated:
        if request.user.is_recruiter:
            return redirect('r_viewprofile')
        return redirect('browse')

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
        return redirect('browse')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.is_recruiter:
                return redirect('r_viewprofile')
            return redirect('browse')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
	return redirect('home')
