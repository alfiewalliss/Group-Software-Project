from django.db import models

# Create your models here.

class task(models.Model):
    taskName = models.CharField(max_length=120)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
