from django.urls import path, include

from .views import students, recruiters, authentication

urlpatterns = [
	path('browse/', authentication.browse, name='browse'),
	path('profile/create/', recruiters.create_profile, name='r_createprofile'),
	path('profile/', recruiters.view_profile, name='r_viewprofile'),
	path('profile/edit', recruiters.edit_profile, name='r_editprofile'),
]