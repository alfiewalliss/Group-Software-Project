from django.contrib import admin
from .models import profile, task

# Register your models here.

admin.site.register(task)
admin.site.register(profile)