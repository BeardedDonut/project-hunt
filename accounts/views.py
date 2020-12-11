from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def logout(request):
    # TODO: Implement
    return HttpResponse('logout!')

def login(request):
    # TODO: Implement
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        # check if the `password` and `confirm_password` match
        if request.POST['password'] == request.POST['confirm_password']:
            # check if the `username` is available
            try:
                user_found = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html'
                , {'error': 'Sorry, this username is not available.'})

            except User.DoesNotExist:
                user =  User.objects.create_user(request.POST['username']
                , password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html'
            , {'error': 'Passwords do not match.'})



    elif request.method == 'GET':
        return render(request, 'accounts/signup.html')
