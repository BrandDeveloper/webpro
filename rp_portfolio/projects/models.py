from django.db import models
import os
from django.conf import settings

def images_path():
    return os.path.join(settings.BASE_DIR, 'static/img')

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    technology = models.CharField(max_length = 20)
    image = models.FilePathField(path=images_path)