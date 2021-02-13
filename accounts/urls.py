from django.urls import path, include

from .views import students, recruiters, authentication

urlpatterns = [
	path('', authentication.browse, name='browse'),


	path('profile/', recruiters.edit_profile, name='profile'),
	path('profile/create', recruiters.create_profile, name='createprofile'),

]