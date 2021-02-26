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

class Skill(models.Model):
	SKILLS = (
		('c++','C++'),
		('java', 'Java')
		)
	name = models.CharField(max_length=50, choices=SKILLS)

	def __str__(self):
		return self.name


class Interest(models.Model):
	name = models.CharField(max_length=50)

class Experience(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()

class StudentProfile(models.Model):
	user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	school = models.CharField(max_length=100)
	graduation_year = models.IntegerField()
	major = models.CharField(max_length=100)

	# skills = models.ManyToManyField(Skill, blank=True, null=True)
	# interests = models.ManyToManyField(Interest, blank=True, null=True)

	def __str__(self):
		return self.user.username





