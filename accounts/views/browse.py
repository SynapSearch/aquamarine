from jobs.models import Job
from ..models import Experience, Project, RecruiterProfile, StudentProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

@login_required
def browse(request, curr=0):
    if request.user.is_recruiter:
        return redirect('r_viewprofile')

    job_array = Job.objects.all()

    if curr != 0:
        last_job = job_array[curr-1]
    else:
        last_job = job_array[0]
    if request.method == 'POST':
        if request.POST['submit'] == 'accepted':
            student = StudentProfile.objects.get(user=request.user)
            student.save()
            last_job.students_who_swiped_yes.add(student)
    if curr == Job.objects.count():
        return redirect('s_viewprofile')
    
    job = job_array[curr]
    curr = curr + 1
    context = {'job': job, "curr":curr}

    return render(request, 'browse.html', context)


@login_required
def r_browse(request, pk):
    if not request.user.is_recruiter:
        return redirect('s_viewprofile')

    student = StudentProfile.objects.first()
    exp = Experience.objects.filter(created_by=student.user)
    project = Project.objects.filter(created_by=student.user)
    context = {'student': student, 'exp': exp, 'project': project}
    
    return render(request, 'browse.html', context)


def home(request):
    if request.user.is_authenticated:
        if request.user.is_recruiter:
            return redirect('r_viewprofile')
        elif request.user.is_superuser:
            return redirect(reverse('admin:index'))
        return redirect('browse', 0)

    return render(request, 'home.html')