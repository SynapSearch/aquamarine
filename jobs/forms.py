from django import forms
from .models import Job

class CreateJobForm(forms.ModelForm):
    class Meta: 
        model = Job
        fields = [
            'title',
            'description',
            'is_remote',
            'term',
            'requirements',
            'preferences'
            ]
