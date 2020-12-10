from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def logout(request):
    # TODO: Implement
    return HttpResponse('logout!')

def login(request):
    # TODO: Implement
    return render(request, 'accounts/login.html')

def signup(request):
    # TODO: Implement
    return render(request, 'accounts/signup.html')
