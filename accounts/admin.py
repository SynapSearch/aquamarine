from django.contrib import admin

# Register your models here.

from .models import (UserProfile, RecruiterProfile)

admin.site.register(UserProfile)
admin.site.register(RecruiterProfile)
