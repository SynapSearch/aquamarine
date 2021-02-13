from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from ..models import *
from ..forms import *


@login_required
def create_profile(request):
	if request.method == 'POST':
		form = RecruiterForm(request.POST)
		if form.is_valid():
			user = request.user
			profile = form.save()
			return redirect('browse')
	else:
		form = RecruiterForm()
	return render(request, 'recruiters/recruiter_profile.html', {'form': form})

@login_required
def edit_profile(request):
	profile = get_object_or_404(RecruiterProfile, pk=profile_id, created_by=request.user)
	if request.method == 'POST':
		form = RecruiterForm(request.POST, instance=profile)

		if form.is_valid():
			profile = form.save(commit=False)
			return redirect('browse')

	else:
		form = RecruiterForm(instance=profile)

	return render(request, 'recruiters/recruiter_profile.html',{'form':form, 'profile':profile})