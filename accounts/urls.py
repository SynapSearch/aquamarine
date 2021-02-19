from django.urls import path, include

from .views import students, recruiters, authentication

urlpatterns = [
	path('browse/', authentication.browse, name='browse'),
	
	path('recruiters/profile/', recruiters.view_profile, name='r_viewprofile'),
	path('recruiters/profile/create/', recruiters.create_profile, name='r_createprofile'),
	path('recruiters/profile/edit', recruiters.edit_profile, name='r_editprofile'),

	path('students/profile/', students.view_profile, name='s_viewprofile'),
	path('students/profile/create', students.create_profile, name='s_createprofile'),
	path('students/profile/edit', students.edit_profile, name='s_editprofile')
]