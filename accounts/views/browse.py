from jobs.models import Job
from ..models import Experience, Project, RecruiterProfile, StudentProfile, Involvement
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

@login_required
def browse(request):
    if request.user.is_recruiter:
        return redirect('r_viewprofile')

    student = StudentProfile.objects.get(user=request.user)
    student.save()
    job_array = Job.objects.exclude(student_has_swiped=student)

    if job_array.count() == 0:
        return redirect('out_of_range')

    job = job_array[0]

    if request.method == 'POST':
        job.student_has_swiped.add(student)
        if request.POST['submit'] == 'accepted':
            job.students_who_swiped_yes.add(student)
        return redirect('browse')

    recruiter = RecruiterProfile.objects.get(user=job.created_by)
    context = {'job': job, 'recruiter':recruiter}

    return render(request, 'browse.html', context)

@login_required
def r_browse(request, pk):
    if not request.user.is_recruiter:
        return redirect('s_viewprofile')

    job = Job.objects.get(pk=pk)
    job.save()

    student_array = job.students_who_swiped_yes.exclude(recruiter_has_swiped_for_job=job)

    if student_array.count() == 0:
        return redirect('out_of_range')

    student = student_array[0]

    if request.method == 'POST':
        job.recruiter_has_swiped.add(student)
        if request.POST['submit'] == 'accepted':
            job.students_accepted_by_recruiter.add(student)
        return redirect('r_browse', pk)

    exp = Experience.objects.filter(created_by=student.user)
    project = Project.objects.filter(created_by=student.user)
    involvement = Involvement.objects.filter(created_by=student.user)
    context = {
    'student': student, 'exp': exp, 'project': project, "involvement":involvement, 
    'curr_pk': pk,}
    
    return render(request, 'browse.html', context)

def home(request):
    if request.user.is_authenticated:
        if request.user.is_recruiter:
            return redirect('r_viewprofile')
        elif request.user.is_superuser:
            return redirect(reverse('admin:index'))
        return redirect('browse')

    return render(request, 'home.html')


def out_of_range(request):
    return render(request, "out_of_range.html")