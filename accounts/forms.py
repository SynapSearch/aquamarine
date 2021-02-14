from django import forms
from .models import UserProfile, RecruiterProfile
from django.db import models, transaction
from django.contrib.auth.forms import UserCreationForm


class UserSignupForm(UserCreationForm):
	class Meta:
		model = UserProfile
		fields = ['username','password1','password2','is_recruiter']

	username = forms.EmailField(max_length=255, error_messages={'required': 'Please enter a valid email address.'})

class RecruiterProfileForm(forms.ModelForm):
	class Meta:
		model = RecruiterProfile
		fields = ['title', 'description', 'location']
