from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'locationgameapp'
urlpatterns = [
    path('', views.index, name='index'),

    path('Game/', views.Game, name='Game'),

    path('AddLocations/', views.AddLocations, name='AddLocations'),

    path('AddAdmin/', views.AddAdmin, name='AddAdmin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
