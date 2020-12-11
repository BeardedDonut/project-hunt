from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from django.utils import timezone

def homepage(request):
    return render(request, 'projects/home.html')

@login_required
def create_project(request):
    if request.method == 'POST':
        if (request.POST['title']
            and request.POST['url']
            and request.POST['project_desc']
            and request.FILES['icon']
            and request.FILES['image']):

            project = Project()
            project.title = request.POST['title']
            project.project_desc = request.POST['project_desc']
            project.icon = request.FILES['icon']
            project.image = request.FILES['image']
            project.date_created = timezone.datetime.now()
            project.total_votes = 1
            project.owner = request.user


            if (request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://')):
                project.url = request.POST['url']
            else:
                project.url = 'http://' + request.POST['url']

            project.save()
            return redirect('home') #TODO: redirect to a page to where project is shown

        else:
            return render(request, 'projects/create.html', {'error': 'All fields are required'})


    else:
        return render(request, 'projects/create.html', )
