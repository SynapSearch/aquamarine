from django.shortcuts import render, redirect
from ..models import UserProfile, RecruiterProfile, StudentProfile, Experience, Project
from ..forms import UserSignupForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from jobs.models import Job



# Create your views here.

@login_required
def browse(request):
    if request.user.is_recruiter:
        ## replace with actual helper function that has a mathing alg 
        options = StudentProfile.objects.first()
        exp = Experience.objects.filter(created_by=options.user)
        project = Project.objects.filter(created_by=options.user)
        context = {'options': options, 'exp': exp, 'project': project}
    else:
        ## replace with actual function that has a mathing alg 
        options = RecruiterProfile.objects.first()
        job = Job.objects.filter(created_by=options.user).first()
        context = {'options': options, 'job': job}
        print(options)
        
    
    return render(request, 'browse.html', context)

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
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('browse')
    

    return render(request, 'login.html', {})


def logout(request):
	return redirect('home')
