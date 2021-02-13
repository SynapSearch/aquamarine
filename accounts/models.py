from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class MyUserManager(BaseUserManager):
	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('The Email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		return self._create_user(email, password, **extra_fields)

class UserProfile(AbstractUser):
	# Using email instead of username
	email = models.EmailField(unique=True)
	objects = MyUserManager()
	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

    # Custom attributes
	is_recruiter = models.BooleanField(default=False)
	def __str__(self):
		return self.email

UserProfile.userprofile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])


class RecruiterProfile(models.Model):
	# IMPORTANT - The related_name is what allows the HTML files to access this classes properties!!
	user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
	title = models.CharField(max_length=150)
	description = models.TextField()
	location = models.CharField(max_length=150)
	def __str__(self):
		return self.user.email

class StudentProfile(models.Model):
	user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
	def __str__(self):
		return user.email



