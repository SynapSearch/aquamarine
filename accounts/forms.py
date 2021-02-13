from django import forms
from .models import UserProfile, RecruiterProfile, StudentProfile
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm


class UserSignupForm(UserCreationForm):
	class Meta():
		model = UserProfile
		fields = ['email','password1','password2','is_recruiter']

	email = forms.EmailField(max_length=255, error_messages={'required': 'Please enter a valid email address.'})


class RecruiterForm(forms.ModelForm):
	class Meta():
		model = RecruiterProfile
		fields = ['title', 'description', 'location',]