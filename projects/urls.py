from django.contrib import admin
from django.urls import path
import projects.views

urlpatterns = [
    path('create/', projects.views.create_project, name='project_create'),
]
