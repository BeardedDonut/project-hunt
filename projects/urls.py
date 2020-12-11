from django.contrib import admin
from django.urls import path
import projects.views

urlpatterns = [
    path('create/', projects.views.create_project, name='project_create'),
    path('<int:project_id>', projects.views.get_project, name='get_project'),
    path('<int:project_id>/upvote', projects.views.upvote_project, name='upvote_project'),
]
