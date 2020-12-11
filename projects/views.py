from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from django.utils import timezone

def homepage(request):
    return render(request, 'projects/home.html')


def get_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def upvote_project(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, pk=project_id)
        project.total_votes += 1
        project.save()
        return redirect('/projects/' + str(project_id))



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
            return redirect('/projects/' + str(project.id))

        else:
            return render(request, 'projects/create.html', {'error': 'All fields are required'})


    else:
        return render(request, 'projects/create.html', )
