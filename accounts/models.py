from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class UserProfile(AbstractUser):
	is_recruiter = models.BooleanField(default=False)
	def __str__(self):
		return self.username

class RecruiterProfile(models.Model):
	# IMPORTANT - The related_name is what allows the HTML files to access this classes properties!!
	user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
	title = models.CharField(max_length=150, validators=[MinLengthValidator(2)])
	description = models.TextField(validators=[MinLengthValidator(2)])
	location = models.CharField(max_length=150, validators=[MinLengthValidator(2)])
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

# Needs to be defined by recruiters
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

class Involvement(models.Model):
	created_by = models.ForeignKey(UserProfile, related_name='involvement', on_delete=models.CASCADE)
	position = models.CharField(max_length=100)
	orginzation = models.CharField(max_length=100)

	def __str__(self):
		return self.title 

class Experience(models.Model):
	created_by = models.ForeignKey(UserProfile, related_name='experience', on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	dates = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.title 

class Project(models.Model):
	created_by = models.ForeignKey(UserProfile, related_name='project', on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	dates = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.title 





