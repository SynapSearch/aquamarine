from django.contrib import admin

# Register your models here.

from .models import (UserProfile, RecruiterProfile,
					StudentProfile, Experience, Project)

admin.site.register(UserProfile)
admin.site.register(RecruiterProfile)
admin.site.register(StudentProfile)
admin.site.register(Experience)
admin.site.register(Project)
