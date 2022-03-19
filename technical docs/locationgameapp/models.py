'''Database models '''

from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class task(models.Model):

    '''Model for the task table
    Includes : taskName - Name of the task
    description - Description of the task
    longitude - Longitude coordinate for the location of the task
    latitude - Latitude coordinate for the location of the task'''

    taskName = models.CharField(max_length=120)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profilePictures')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            outputSize = (300,300)
            img.thumbnail(outputSize)
            img.save(self.image.path)
