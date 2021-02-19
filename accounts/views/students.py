from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import UserProfile, StudentProfile
from ..forms import StudentProfileForm
from django.db import models

@login_required
def create_profile(request):
	if request.method == 'POST':
		form = StudentProfileForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.skills.add(form.cleaned_data.get('skills'))
			profile.save()
			return redirect('s_viewprofile')
	else:
		form = StudentProfileForm()

	return render(request, 'students/student_create_profile.html', {'form':form})

@login_required
def view_profile(request):
	profile = get_object_or_404(StudentProfile, user=request.user)
	return render(request, 'students/student_view_profile.html', {'profile':profile})

@login_required
def edit_profile(request):
	profile = get_object_or_404(StudentProfile, user=request.user)
	if request.method == 'POST':
		form = StudentProfileForm(request.POST, instance=profile)
		if form.is_valid():
			profile = form.save()
			profile.save()
			return redirect('s_viewprofile')
	else:
		form = RecruiterProfileForm(instance=profile)

	return render(request, 'students/student_edit_profile.html', {'form':form})