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
    job_array = Job.objects.exclude(student_has_swiped=student)

    if job_array.count() == 0:
        return redirect('out_of_range')

    job = job_array[0]

    if request.method == 'POST':
        if request.POST['submit'] == 'accepted':
            job.students_who_swiped_yes.add(student)
            job.student_has_swiped.add(student)
        elif request.POST['submit'] == 'rejected':
            job.student_has_swiped.add(student)
        elif request.POST['submit'] == 'back':
            temp_job = Job.objects.filter(student_has_swiped=student).last()
            temp_job.student_has_swiped.remove(student)
            temp_job.students_who_swiped_yes.remove(student)
        return redirect('browse')

    recruiter = RecruiterProfile.objects.get(user=job.created_by)
    context = {'job': job, 'recruiter':recruiter}

    return render(request, 'browse.html', context)

@login_required
def r_browse(request, pk):
    if not request.user.is_recruiter:
        return redirect('s_viewprofile')

    job = Job.objects.get(pk=pk)

    student_array = job.students_who_swiped_yes.exclude(recruiter_has_swiped_for_job=job)

    if student_array.count() == 0:
        return redirect('out_of_range')

    student = student_array[0]

    if request.method == 'POST':
        if request.POST['submit'] == 'accepted':
            job.recruiter_has_swiped.add(student)
            job.students_accepted_by_recruiter.add(student)
        elif request.POST['submit'] == 'maybe':
            job.students_in_maybe_pile.add(student)
            job.recruiter_has_swiped.add(student)
        elif request.POST['submit'] == 'rejected':
            job.recruiter_has_swiped.add(student)
        elif request.POST['submit'] == 'back':
            temp_student = job.recruiter_has_swiped.last()
            job.recruiter_has_swiped.remove(temp_student)
            job.students_in_maybe_pile.remove(temp_student)

        return redirect('r_browse', pk)

    exp = Experience.objects.filter(created_by=student.user)
    project = Project.objects.filter(created_by=student.user)
    involvement = Involvement.objects.filter(created_by=student.user)
    maybe_browse_is_true = False;

    context = {
    'student': student, 'exp': exp, 'project': project, "involvement":involvement, 
    'curr_pk': pk, 'maybe_browse_is_true': maybe_browse_is_true}
    
    return render(request, 'browse.html', context)

@login_required
def maybe_browse(request, pk):
    if not request.user.is_recruiter:
        return redirect('s_viewprofile')

    job = Job.objects.get(pk=pk)

    student_array = job.students_in_maybe_pile.all().exclude(temp_maybe_list_for_job=job)

    if student_array.count() == 0:
        return redirect('out_of_range')

    student = student_array[0]

    if request.method == 'POST':
        if request.POST['submit'] == 'accepted':
            job.students_accepted_by_recruiter.add(student)
            job.students_in_maybe_pile.remove(student)
        elif request.POST['submit'] == 'maybe':
            job.temp_maybe_list.add(student)
        elif request.POST['submit'] == 'rejected':
            job.students_in_maybe_pile.remove(student)
        elif request.POST['submit'] == 'back':
            temp_student = job.temp_maybe_list.last()
            job.temp_maybe_list.remove(temp_student)

        return redirect('maybe_browse', pk)

    exp = Experience.objects.filter(created_by=student.user)
    project = Project.objects.filter(created_by=student.user)
    involvement = Involvement.objects.filter(created_by=student.user)
    maybe_browse_is_true = True;

    context = {
    'student': student, 'exp': exp, 'project': project, "involvement":involvement, 
    'curr_pk': pk, 'maybe_browse_is_true': maybe_browse_is_true}

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