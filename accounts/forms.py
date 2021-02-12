from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

	username = forms.EmailField(max_length=255, error_messages={'required': 'Please enter a valid email address.'})
	password1 = forms.CharField(widget=forms.PasswordInput, required=True)

