from django.urls import path, include

from .views import students, recruiters, authentication

urlpatterns = [
	path('signup/', authentication.signup, name="signup"),
	path('login/', authentication.login_view, name="login"),
	path('browse/', authentication.browse, name='browse'),
	
	path('recruiters/profile/', recruiters.view_profile, name='r_viewprofile'),
	path('recruiters/profile/create/', recruiters.create_profile, name='r_createprofile'),
	path('recruiters/profile/edit', recruiters.edit_profile, name='r_editprofile'),

	path('students/profile/', students.view_profile, name='s_viewprofile'),
	path('students/profile/create', students.create_profile, name='s_createprofile'),
	path('students/profile/edit', students.edit_profile, name='s_editprofile'),

	path('students/profile/edit/create/expirence', students.create_experience, name='s_createexp'),
	path('students/profile/edit/create/project', students.create_project, name='s_createproject')
]