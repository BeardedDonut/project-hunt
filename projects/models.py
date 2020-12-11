from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    url = models.TextField(max_length=250)
    date_created = models.DateTimeField()
    total_votes = models.IntegerField(default = 1)
    image = models.ImageField(upload_to='images/project_images/')
    icon = models.ImageField(upload_to='images/icon_images/')
    project_desc = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def print_pretty_date_created(self):
        '''
        Returns a pretty format of the `created_date` like 'December 4th 2020'
        '''
        return self.date_created.strftime('%b %e %Y')


    def project_summary(self):
        '''
        Returns the first 100 characters of the `project_desc`
        '''
        return self.project_desc[:100] + '...'


    def __str__(self):
        '''
        Returns `title`

        This helps to find the projects easier in the admin panel
        '''
        return self.title
