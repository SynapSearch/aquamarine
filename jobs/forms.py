from django import forms
from .models import Job

class CreateJobForm(forms.ModelForm):
    class Meta: 
        model = Job
        fields = [
            'title',
            'description',
            'location',
            # 'catagory',
            'term',
            'requirments',
            'prefences'
            ]