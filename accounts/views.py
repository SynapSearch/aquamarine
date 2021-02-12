from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserSignupForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
	return render(request, 'home.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        if 'signupbutton' in request.POST:
            form = UserSignupForm(request.POST)

            if form.is_valid():
                user = form.save()
                account_type = request.POST.get('account_type', 'jobseeker')

                if account_type == 'employer':
                    userprofile = UserProfile.objects.create(user=user, is_recruiter=True)
                    userprofile.save()
                else:
                    userprofile = UserProfile.objects.create(user=user)
                    userprofile.save()

                login(request, user)

                return redirect('home')
        elif 'loginbutton' in request.POST:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home')
    else:
        form = UserSignupForm()

    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
	return redirect('home')
