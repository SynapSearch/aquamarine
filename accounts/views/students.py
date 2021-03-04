from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import UserProfile, StudentProfile, Project, Experience, Skill, Interest
from ..forms import StudentProfileForm, ProjectForm, ExperienceForm
from django.db import models

@login_required
def create_profile(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('s_viewprofile')

	if not Skill.objects.exists():
		Skill.objects.bulk_create([Skill(name='0'),Skill(name='1'),])
	if not Interest.objects.exists():
		Interest.objects.bulk_create([Interest(name='0'),Interest(name='1'),])

	if request.method == 'POST':
		form = StudentProfileForm(request.POST)
		if form.is_valid():
			profile = form.save()
			profile.user = request.user
			skills = request.POST.getlist('skills')
			interests = request.POST.getlist('interests')
			for s in skills:
				s = Skill.objects.get_or_create(name=s)[0]
				s.save()
				profile.skills.add(s)
			for i in interests:
				i = Interest.objects.get_or_create(name=i)[0]
				i.save()
				profile.interests.add(i)
			profile.save()
			return redirect('s_viewprofile')
		else:
			form = StudentProfileForm()
	else:
		form = StudentProfileForm()

	interest_list = Interest.objects.all()
	skill_list = Skill.objects.all()
	context = {'form':form, 'skill_list':skill_list, 'interest_list': interest_list}

	return render(request, 'students/student_create_profile.html', context)

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
def edit_experience(request, pk):
	exp = get_object_or_404(Experience, pk=pk)
	if request.method == 'POST':
		form = ExperienceForm(request.POST, instance=exp)
		if form.is_valid():
			exp = form.save()
			exp.save()
			return redirect('s_viewprofile')
	else:
		form = ExperienceForm(instance=exp)

	return render(request, 'students/student_edit_exp.html', {'form':form})


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


@login_required
def edit_project(request, pk):
	project = get_object_or_404(Project, pk=pk)
	if request.method == 'POST':
		form = ProjectForm(request.POST, instance=project)
		if form.is_valid():
			project = form.save()
			project.save()
			return redirect('s_viewprofile')
	else:
		form = ProjectForm(instance=project)

	return render(request, 'students/student_edit_project.html', {'form':form})
