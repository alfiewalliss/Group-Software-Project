from django.contrib import admin
from .models import profile, task, pleaderboard

# Register your models here.

admin.site.register(task)
admin.site.register(profile)
admin.site.register(pleaderboard)