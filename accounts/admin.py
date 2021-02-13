from django.contrib import admin

# Register your models here.

from .models import (UserProfile, RecruiterProfile, 
					StudentProfile)

admin.site.register(UserProfile)
admin.site.register(RecruiterProfile)
admin.site.register(StudentProfile)