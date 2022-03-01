'''All database models '''

from django.db import models

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
