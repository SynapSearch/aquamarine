from django.shortcuts import render, redirect

# Create your views here.
# Create your views here.
from django.shortcuts import render, get_object_or_404

from .models import Job
from .forms import CreateJobForm
from django.db.models import Q


def create_jobs(request, *args, **kargs):
    form = CreateJobForm(request.POST)
    if form.is_valid():
        newjob = form.save(commit=False)
        newjob.created_by = request.user
        newjob.save()
        return redirect('r_viewprofile')

    context = {
        'form':form,
    }
    return render(request, "create_job.html", context)
