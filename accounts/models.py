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
	picture = models.ImageField(upload_to="gallery", default="gallery/profile_pic_default.png", blank=True)

	def __str__(self):
		return self.user.username

class Interest(models.Model):
	INTERESTS = (
		('0','Machine Learning'),
		('1','Biology'),
		)
	name = models.CharField(max_length=50, choices=INTERESTS)

	def __str__(self):
		return self.name

class Skill(models.Model):
	SKILLS = (
		('0','C++'),
		('1', 'Java'),
		)
	name = models.CharField(max_length=50, choices=SKILLS)

	def __str__(self):
		return self.name

class StudentProfile(models.Model):
	user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	school = models.CharField(max_length=100)
	graduation_year = models.IntegerField()
	major = models.CharField(max_length=100)

	picture = models.ImageField(upload_to="gallery", default="gallery/profile_pic_default.png", blank=True, null=True)

	skills = models.ManyToManyField(Skill)
	interests = models.ManyToManyField(Interest)

	def __str__(self):
		return self.user.username

class Experience(models.Model):
	created_by = models.ForeignKey(UserProfile, related_name='experience', on_delete=models.CASCADE)
	title = models.TextField()
	company = models.TextField(default="none")
	dates = models.TextField(default="none")
	description = models.TextField()

	def __str__(self):
		return self.title 

class Project(models.Model):
	created_by = models.ForeignKey(UserProfile, related_name='project', on_delete=models.CASCADE)
	title = models.TextField()
	company = models.TextField()
	dates = models.TextField()
	description = models.TextField()

	def __str__(self):
		return self.title 





