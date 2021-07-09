from django import forms
from .models import UserProfile, RecruiterProfile, StudentProfile, Experience, Project, Involvement
from django.db import models, transaction
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

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

class UserLoginForm(AuthenticationForm):
	class Meta:
		model = UserProfile
		fields = ['username', 'password']
	username = forms.EmailField(max_length=255, 
		widget=forms.TextInput(attrs={'placeholder':'Email'}),
		error_messages={'required': 'Please enter a valid email address.'})
	password = forms.CharField(max_length=255,
		widget=forms.PasswordInput(attrs={'placeholder':'Password'}),
		error_messages={'required': 'Passwords must be at least 8 characters long.'})

class RecruiterProfileForm(forms.ModelForm):
	class Meta:
		model = RecruiterProfile
		fields = ['title', 'description', 'location', 'picture']

class StudentProfileForm(forms.ModelForm):
	class Meta:
		model = StudentProfile
		fields = ['first_name', 'last_name', 'school', 'graduation_year', 'major', 'picture']

	first_name = forms.CharField(max_length=13, validators=[MinLengthValidator(2)],
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
        error_messages={'required': 'First name must be at least 2 characters but no more than 13 characters'})
	last_name = forms.CharField(max_length=13, validators=[MinLengthValidator(2)],
		widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
		error_messages={'required': 'Last name must be at least 2 characters but no more than 13 characters'})
	school = forms.CharField(max_length=100, validators=[MinLengthValidator(2)], 
		widget=forms.TextInput(attrs={'placeholder': 'School'}),
		error_messages={'required': 'School must not exceed 100 characters'})
	graduation_year = forms.IntegerField(validators=[MinValueValidator(2010), MaxValueValidator(2030)],
		widget=forms.TextInput(attrs={'placeholder': 'Graduation Year'}),
		error_messages={'required': 'Graduation Year entered must be between 2010 to 2030'})
	major = forms.CharField(max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Major'}),
		error_messages={'required': 'Major must not exceed 100 characters'})
    # add picture?

class ExperienceForm(forms.ModelForm):
	class Meta: 
		model = Experience
		fields = ['title', 'company', 'dates', 'description']

class ProjectForm(forms.ModelForm):
	class Meta: 
		model = Project
		fields = ['title', 'company', 'dates', 'description']


class InvolvementForm(forms.ModelForm):
	class Meta:
		model = Involvement
		fields = ["position", "orginzation"]