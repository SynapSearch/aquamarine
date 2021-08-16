from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
import tagulous.models
from django.urls import reverse

class UserProfile(AbstractUser):
	is_recruiter = models.BooleanField(default=False)
	def __str__(self):
		return self.username

class RecruiterProfile(models.Model):
	# IMPORTANT - The related_name is what allows the HTML files to access this classes properties!!
	user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
	title = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(2)])
	description = models.TextField(validators=[MaxLengthValidator(500), MinLengthValidator(2)])
	location = models.CharField(max_length=100,validators=[MaxLengthValidator(100), MinLengthValidator(2)])
	picture = models.ImageField(upload_to="gallery", default="gallery/profile_pic_default.png", blank=True)

	def __str__(self):
		return self.user.username

class Interest(tagulous.models.TagTreeModel):
    class TagMeta:
        initial = [
            "Python/Django",
            "Python/Flask",
            "JavaScript/JQuery",
            "JavaScript/Angular.js",
            "Linux/nginx",
            "Linux/uwsgi",
        ]
        space_delimiter = False
        autocomplete_view = "StudentProfile_interests_autocomplete"


class Skill(tagulous.models.TagTreeModel):
    class TagMeta:
        initial = [
            "Python/Django",
            "Python/Flask",
            "JavaScript/JQuery",
            "JavaScript/Angular.js",
            "Linux/nginx",
            "Linux/uwsgi",
        ]
        space_delimiter = False
        autocomplete_view = "StudentProfile_skills_autocomplete"

class StudentProfile(models.Model):
	user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	school = models.CharField(max_length=100)
	graduation_year = models.IntegerField()
	major = models.CharField(max_length=100)

	picture = models.ImageField(upload_to="gallery", default="gallery/profile_pic_default.png", blank=True, null=True)
	skills = tagulous.models.TagField(
        Skill, help_text="This field does not split on spaces", blank=True
    )
	interests = tagulous.models.TagField(
        Interest, help_text="This field does not split on spaces", blank=True
    )

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





