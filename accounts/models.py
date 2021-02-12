from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	# IMPORTANT - The related_name is what allows the HTML files to access this classes properties!!
	user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
	is_recruiter = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

User.user_account = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])
