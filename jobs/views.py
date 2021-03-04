from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404

from .models import Job
from accounts.models import Skill

from .forms import CreateJobForm

def create_jobs(request):
    if not request.user.is_recruiter:
        return redirect('browse')

    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job = form.save()
            requirements = request.POST.getlist('requirements')
            preferences = request.POST.getlist('preferences')
            for i in requirements:
                i = Skill.objects.get_or_create(name=i)[0]
                i.save()
                job.requirements.add(i)
            for p in preferences:
                p = Skill.objects.get_or_create(name=p)[0]
                p.save()
                job.preferences.add(p)
            job.save()
            return redirect('r_viewprofile')
        else:
            form = CreateJobForm()
    else:
        form = CreateJobForm()

    requirements_list = Skill.objects.all()
    preferences_list = Skill.objects.all()
    context = {
        'form':form,
        'requirements_list': requirements_list,
        'preferences_list': preferences_list,
    }
    return render(request, "create_job.html", context)


def edit_jobs(request, pk):
    if not request.user.is_recruiter:
        return redirect('browse')

    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = CreateJobForm(request.POST, instance=job)
        if form.is_valid():
            newjob = form.save()
            newjob.save()
            return redirect('r_viewprofile')
    else:
        form = CreateJobForm(instance=job)

    context = {
        'form':form,
    }
    return render(request, "edit_job.html", context)
