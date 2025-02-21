# Create a new django project

## Set current dir and activate correct virtual env
cd app17-django-form
.venv\Scripts\Activate

## Creates a django project - dir mysite
django-admin startproject mysite .

## Creates the app - dir job_application
python manage.py startapp job_application \
A project can contain multiple apps

## Config
mysite/settings.py --> add name of app to INSTALLED_APPS list

## Running a django app
python manage.py runserver

## Django docs
https://docs.djangoproject.com/en/5.1/

## Migrations
Models are defined in job_application/models.py \
python manage.py makemigrations \
python manage.py migrate

## Send email
mysite/settings.py needs config for smtp provider \
django.core.mail provides high-level email support

## Create admin interface
python manage.py createsuperuser \
"your_app_dir"/admin.py only needs 2 lines of code to implement admin for a given model: \
from .models import Form \
admin.site.register(Form)