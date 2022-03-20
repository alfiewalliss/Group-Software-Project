from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from locationgameapp import models

@receiver(post_save, sender=User)
def createProfile(sender, instance, created,*args, **kwargs):
    if created:
        models.profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveProfile(sender, instance,*args,  **kwargs):
    instance.profile.save()