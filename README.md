# TopOfThePile
Commands:


Pip install django-taggit


Creating Virtual Environment: virtualenv -p python3 .
Starting Virtual Environment: source bin/activate


DJANGO
  Install allauth: pip install django-allauth
Install DJango: pip install django
        Make Migrations: python manage.py makemigrations
   	Migrate: python manage.py migrate
       	    Start Server: python manage.py runserver
       Create superuser: python manage.py createsuperuser
            Start New App: python manage.py startapp
   Start Project: django-admin startproject ‘projectname’
Condense Static: python manage.py collectstatic
Delete Migrations:  find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete   
 
 




GITHUB
       Clone repository: git clone
                     add files: git add
              commit files: git commit ‘file’ -m ‘commit message’
  push files to github: git push -u origin ‘branch’
           create branch: git checkout -b ‘newbranchname’
         change branch: git checkout ‘branch’
           pull files from github: git pull origin ‘branch’
