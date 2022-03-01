'''/admin page -
Displays the current data inside the databases
using models provided from models.py'''

from django.contrib import admin
from .models import task

# Register your models here.

admin.site.register(task)
