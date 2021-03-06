from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import UserProfile, RecruiterProfile
from ..forms import RecruiterProfileForm
from django.db import models
from jobs.models import Job

@login_required
def create_profile(request):
	if RecruiterProfile.objects.filter(user=request.user).exists():
		return redirect('r_viewprofile')
		
	if request.method == 'POST':
		form = RecruiterProfileForm(request.POST,  request.FILES)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			return redirect('r_viewprofile')
	else:
		form = RecruiterProfileForm()

	return render(request, 'recruiters/recruiter_create_profile.html', {'form':form})

@login_required
def view_profile(request):
	profile = get_object_or_404(RecruiterProfile, user=request.user)
	if "pic" in request.FILES and "sub" in request.POST:
		profile.picture = request.FILES["pic"]
		profile.save()
	for i in Job.objects.all():
		i.temp_maybe_list.clear()
	jobs = Job.objects.filter(created_by=request.user)
	return render(request, 'recruiters/recruiter_view_profile.html', {'profile':profile, 'jobs':jobs})

@login_required
def edit_profile(request):
	profile = get_object_or_404(RecruiterProfile, user=request.user)
	if request.method == 'POST':
		form = RecruiterProfileForm(request.POST,  request.FILES, instance=profile)
		if form.is_valid():
			profile = form.save()
			profile.save()
			return redirect('r_viewprofile')
	else:
		form = RecruiterProfileForm(instance=profile)

	return render(request, 'recruiters/recruiter_edit_profile.html', {'form':form})
