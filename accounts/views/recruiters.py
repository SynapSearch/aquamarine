from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import UserProfile, RecruiterProfile
from ..forms import RecruiterProfileForm
from django.db import models

@login_required
def create_profile(request):
	if request.method == 'POST':
		form = RecruiterProfileForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			return redirect('viewprofile')
	else:
		form = RecruiterProfileForm()

	return render(request, 'recruiters/recruiter_create_profile.html', {'form':form})

@login_required
def view_profile(request):
	profile = get_object_or_404(RecruiterProfile, user=request.user)
	return render(request, 'recruiters/recruiter_view_profile.html', {'profile':profile})

@login_required
def edit_profile(request):
	profile = get_object_or_404(RecruiterProfile, user=request.user)
	if request.method == 'POST':
		form = RecruiterProfileForm(request.POST, instance=profile)
		if form.is_valid():
			profile = form.save()
			profile.save()
			return redirect('viewprofile')
	else:
		form = RecruiterProfileForm(instance=profile)

	return render(request, 'recruiters/recruiter_edit_profile.html', {'form':form})


