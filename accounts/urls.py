from django.contrib import admin
from django.urls import path
import accounts.views

urlpatterns = [
    path('', accounts.views.login, name='account_login'),
    path('login/', accounts.views.login, name='account_login'),
    path('logout/', accounts.views.logout, name='account_logout'),
    path('signup/', accounts.views.signup, name='account_signup'),
]
