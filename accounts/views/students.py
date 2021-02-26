from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import UserProfile, StudentProfile, Project, Experience
from ..forms import StudentProfileForm, ProjectForm, ExperienceForm
from django.db import models

@login_required
def create_profile(request):
	if request.method == 'POST':
		form = StudentProfileForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			return redirect('s_viewprofile')
	else:
		form = StudentProfileForm()

	return render(request, 'students/student_create_profile.html', {'form':form})

@login_required
def view_profile(request):
	profile = get_object_or_404(StudentProfile, user=request.user)
	exp = Experience.objects.filter(created_by=request.user)
	project = Project.objects.filter(created_by=request.user)
	return render(request, 'students/student_view_profile.html', {'profile':profile, 'exp':exp, 'project':project})

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
		form = StudentProfileForm(instance=profile)

	return render(request, 'students/student_edit_profile.html', {'form':form})

@login_required
def create_experience(request):
	form = ExperienceForm(request.POST)
	if form.is_valid():
		new_exp = form.save(commit=False)
		new_exp.created_by = request.user
		new_exp.save()
		return redirect('s_viewprofile')

	context = {
		'form': form,
	}
	return render(request, "students/student_create_exp.html", context)

@login_required
def create_project(request):
	form = ProjectForm(request.POST)
	if form.is_valid():
		new_exp = form.save(commit=False)
		new_exp.created_by = request.user
		new_exp.save()
		return redirect('s_viewprofile')

	context = {
		'form': form,
	}
	return render(request, "students/student_create_project.html", context)
