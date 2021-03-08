from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404

from .models import Job, Compensation
from accounts.models import Skill

from .forms import CreateJobForm

from itertools import zip_longest

def create_jobs(request):
    if not request.user.is_recruiter:
        return redirect('browse')

    if not Compensation.objects.exists():
        Compensation.objects.bulk_create(
        [Compensation(name='0'),
        Compensation(name='1'),
        Compensation(name='2'),
        Compensation(name='3'),
        Compensation(name='4'),
        ])

    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job = form.save()
            requirements = request.POST.getlist('requirements')
            preferences = request.POST.getlist('preferences')
            compensation_types = request.POST.getlist('compensation_types')
            for i in requirements:
                i = Skill.objects.get_or_create(name=i)[0]
                i.save()
                job.requirements.add(i)
            for p in preferences:
                p = Skill.objects.get_or_create(name=p)[0]
                p.save()
                job.preferences.add(p)
            for c in compensation_types:
                c = Compensation.objects.get_or_create(name=c)[0]
                c.save()
                job.compensation_types.add(c)
            job.save()
            return redirect('r_viewprofile')
        else:
            form = CreateJobForm()
    else:
        form = CreateJobForm()

    requirements_list = Skill.objects.all()
    preferences_list = Skill.objects.all()
    compensation_list = Compensation.objects.all()
    context = {
        'form':form,
        'requirements_list': requirements_list,
        'preferences_list': preferences_list,
        'compensation_list': compensation_list,
    }
    return render(request, "jobs/create_job.html", context)

def edit_jobs(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')

    if not request.user.is_recruiter:
        return redirect('browse')

    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = CreateJobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save()
            job.compensation_types.clear()
            compensation_types = request.POST.getlist('compensation_types')
            for c in compensation_types:
                c = Compensation.objects.get_or_create(name=c)[0]
                c.save()
                job.compensation_types.add(c)
            job.save()
            return redirect('r_viewprofile')
    else:
        form = CreateJobForm(instance=job)

    requirements_list = Skill.objects.all()
    preferences_list = Skill.objects.all()
    compensations_saved = list(job.compensation_types.all())
    compensation_list = Compensation.objects.all()

    context = {
        'form':form,
        'job': job,
        'requirements_list': requirements_list,
        'preferences_list': preferences_list,
        'compensations_saved': compensations_saved,
        'compensation_list': compensation_list
    }
    return render(request, "jobs/edit_job.html", context)
