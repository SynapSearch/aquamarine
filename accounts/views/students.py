from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import UserProfile, StudentProfile, Project, Experience, Interest, Involvement, Skill
from jobs.models import Job
from ..forms import StudentProfileForm, ProjectForm, ExperienceForm, InvolvementForm, RecruiterProfile
from django.db import models
from django.db.models import Q 
from django.urls import reverse



@login_required
def create_profile(request):
	if StudentProfile.objects.filter(user=request.user).exists():
		return redirect('s_viewprofile')

	skills = Skill.objects.all()
	interests = Interest.objects.all()
	if not Interest.objects.exists():
		Interest.objects.bulk_create([Interest(name='0'),Interest(name='1'),])

	if request.method == 'POST':
		form = StudentProfileForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile = form.save()
			# skills = request.POST.getlist('skills')
			interests = request.POST.getlist('interests')
			# for s in skills:
			# 	s = Skill.objects.get_or_create(name=s)[0]
			# 	s.save()
			# 	profile.skills.add(s)
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
	context = {
		'form':form, 
		'skills':skills, 
		'interests': interests, 
		'form_media': form.media,
		"Interest_name": Interest.__name__,
	}

	return render(request, 'students/student_create_profile.html', context)

@login_required
def view_profile(request):
	profile = get_object_or_404(StudentProfile, user=request.user)
	exp = Experience.objects.filter(created_by=request.user)
	project = Project.objects.filter(created_by=request.user)
	involvement = Involvement.objects.filter(created_by=request.user)
	skills = Skill.objects.all()
	interests = Interest.objects.all()
	print(skills)
	return render(request, 'students/student_view_profile.html', {'profile':profile, 'exp':exp, 'project':project, "involvement": involvement, "skills": skills, "interests": interests})

@login_required
def edit_profile(request):
	profile = get_object_or_404(StudentProfile, user=request.user)
	skills = Skill.objects.all()
	interests = Interest.objects.all()

	if request.method == 'POST':
		
		form = StudentProfileForm(request.POST, request.FILES, instance=profile)
		
		# print("SKILLS", request.POST.getlist('skills'))
		# print("Interests", request.POST.getlist('interests'))
		if form.is_valid():
			
			profile = form.save()
			profile.save()
			return redirect('s_viewprofile')
	else:
		form = StudentProfileForm(instance=profile)
	return render(request, 'students/student_edit_profile.html', {'form':form, "profile":profile, 'skills':skills, 'form_media': form.media,"Skill_name": Skill.__name__, "interests": interests, "Interest_name": Interest.__name__})

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


@login_required
def create_involvement(request):
	form = InvolvementForm(request.POST)
	if form.is_valid():
		new_invol = form.save(commit=False)
		new_invol.created_by = request.user
		new_invol.save()
		return redirect('s_viewprofile')

	context = {
		'form': form,
	}
	return render(request, "students/student_create_involvement.html", context)

@login_required
def edit_involvement(request, pk):
	invol = get_object_or_404(Involvement, pk=pk)
	if request.method == 'POST':
		form = InvolvementForm(request.POST, instance=invol)
		if form.is_valid():
			invol = form.save()
			invol.save()
			return redirect('s_viewprofile')
	else:
		form = InvolvementForm(instance=invol)

	return render(request, 'students/student_edit_involvement.html', {'form':form})

@login_required
def search_results(request):
	query = request.GET.get('q')
	context={"jobs": None, "labs":None}
	if(len(query)>1):
		job_results = Job.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
		lab_results = RecruiterProfile.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
		context["jobs"] = job_results
		context["labs"]=lab_results
	print(job_results)
	return render(request, "search_results.html", context)