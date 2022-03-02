<<<<<<< HEAD
'''Database models '''

=======
>>>>>>> parent of fcb8a67 (Start of linting + Commenting)
from django.db import models

# Create your models here.

class task(models.Model):
<<<<<<< HEAD

    '''Model for the task table
    Includes : taskName - Name of the task
    description - Description of the task
    longitude - Longitude coordinate for the location of the task
    latitude - Latitude coordinate for the location of the task'''

=======
>>>>>>> parent of fcb8a67 (Start of linting + Commenting)
    taskName = models.CharField(max_length=120)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
