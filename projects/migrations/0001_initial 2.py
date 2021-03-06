# Generated by Django 3.1.3 on 2020-12-11 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('url', models.TextField(max_length=250)),
                ('date_created', models.DateTimeField()),
                ('total_votes', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='images/project_images/')),
                ('icon', models.ImageField(upload_to='images/icon_images/')),
                ('project_desc', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
