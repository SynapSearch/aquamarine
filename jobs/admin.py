from django.contrib import admin

# Register your models here.
from .models import Job, Compensation

admin.site.register(Job)
admin.site.register(Compensation)