from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
	is_recruiter = models.BooleanField(default=False)
	def __str__(self):
		return self.username

class RecruiterProfile(models.Model):
	# IMPORTANT - The related_name is what allows the HTML files to access this classes properties!!
	user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
	title = models.CharField(max_length=150)
	description = models.TextField()
	location = models.CharField(max_length=150)
	def __str__(self):
		return self.user.username