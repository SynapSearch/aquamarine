from django.urls import path, include
from django.conf.urls import url


import tagulous.views

from .models import Skill, Interest

from .views import students, recruiters, authentication, browse

urlpatterns = [
	path('signup/', authentication.signup, name="signup"),
	path('login/', authentication.login_view, name="login"),

	path('recruiters/browse/<int:pk>/', browse.r_browse, name='r_browse'),
	path('recruiters/browse/<int:pk>/undecided/', browse.maybe_browse, name='maybe_browse'),
	path('browse/', browse.browse, name='browse'),
	path('end/', browse.out_of_range, name='out_of_range'),
	
	path('recruiters/profile/', recruiters.view_profile, name='r_viewprofile'),
	path('recruiters/profile/create/', recruiters.create_profile, name='r_createprofile'),
	path('recruiters/profile/edit', recruiters.edit_profile, name='r_editprofile'),

	path('students/profile/', students.view_profile, name='s_viewprofile'),
	path('students/profile/create', students.create_profile, name='s_createprofile'),
	path('students/profile/edit', students.edit_profile, name='s_editprofile'),
	path('search/', students.search_results, name='search_results'),
	url(
        r"^api/skills/$",
        tagulous.views.autocomplete,
        {"tag_model": Skill},
        name="StudentProfile_skills_autocomplete",
    ),
	url(
        r"^api/interests/$",
        tagulous.views.autocomplete,
        {"tag_model": Interest},
        name="StudentProfile_interests_autocomplete",
    ),

	path('students/profile/edit/create/expirence', students.create_experience, name='s_createexp'),
	path('students/profile/edit/create/project', students.create_project, name='s_createproject'),
	path('students/profile/edit/expirence/edit/<int:pk>/', students.edit_experience, name='editexp'),
	path('students/profile/edit/project/edit/<int:pk>/', students.edit_project, name='editproject'),
	path('students/profile/edit/create/involvement', students.create_involvement, name ="s_createin"),
	path('students/profile/edit/involvement/edit/<int:pk>/', students.edit_involvement, name ="s_editin"),

]