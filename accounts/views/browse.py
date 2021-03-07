from jobs.models import Job
from ..models import Experience, Project, RecruiterProfile, StudentProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

@login_required
def browse(request, curr=0):
    if Job.objects.count() == 0:
        return redirect('out_of_range')

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
        return redirect('out_of_range')
    
    job = job_array[curr]
    curr = curr + 1
    context = {'job': job, "curr":curr}

    return render(request, 'browse.html', context)

@login_required
def r_browse(request, pk, curr_student=0):

    if not request.user.is_recruiter:
        return redirect('s_viewprofile')

    job = Job.objects.get(pk=pk)
    student_array = job.students_who_swiped_yes.all()

    if student_array.count() == 0:
        return redirect('out_of_range')

    if curr_student != 0:
        last_student = student_array[curr_student-1]
    else:
        last_student = student_array[0]

    if request.method == 'POST':
        if request.POST['submit'] == 'accepted':
            job.students_accepted_by_recruiter.add(last_student)


    if curr_student == student_array.count():
        return redirect('out_of_range')

    student = student_array[curr_student]
    curr_student = curr_student + 1

    exp = Experience.objects.filter(created_by=student.user)
    project = Project.objects.filter(created_by=student.user)
    context = {
    'student': student, 'exp': exp, 'project': project,
    'curr_pk': pk, 'curr_student': curr_student}
    
    return render(request, 'browse.html', context)

def home(request):
    if request.user.is_authenticated:
        if request.user.is_recruiter:
            return redirect('r_viewprofile')
        elif request.user.is_superuser:
            return redirect(reverse('admin:index'))
        return redirect('browse', 0)

    return render(request, 'home.html')


def out_of_range(request):
    return render(request, "out_of_range.html")