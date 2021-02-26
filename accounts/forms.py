from django import forms
from .models import UserProfile, RecruiterProfile, StudentProfile, Skill
from django.db import models, transaction
from django.contrib.auth.forms import UserCreationForm


class UserSignupForm(UserCreationForm):
	class Meta:
		model = UserProfile
		fields = ['username','password1','password2','is_recruiter']

	username = forms.EmailField(max_length=255, 
		widget=forms.TextInput(attrs={'placeholder':'Email'}),
		error_messages={'required': 'Please enter a valid email address.'})
	password1 = forms.CharField(max_length=255,
		widget=forms.PasswordInput(attrs={'placeholder':'Password'}),
		error_messages={'required': 'Passwords must be at least 8 characters long.'})
	password2 = forms.CharField(max_length=255,
		widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),
		error_messages={'required': 'Passwords must match.'})
	is_recruiter= forms.CharField(label='Account type', widget=forms.Select(
		choices=[(False, "Job seeker"), (True, "Employer")]))


class RecruiterProfileForm(forms.ModelForm):
	class Meta:
		model = RecruiterProfile
		fields = ['title', 'description', 'location']

class StudentProfileForm(forms.ModelForm):
	# skills = forms.ModelMultipleChoiceField(queryset=Skill.objects, 
	# 	widget=forms.CheckboxSelectMultiple(), required=False)
	class Meta:
		model = StudentProfile
		fields = ['first_name', 'last_name', 'school',
				'graduation_year', 'major'] #, 'skills']

