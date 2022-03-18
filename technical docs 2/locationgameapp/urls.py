from unicodedata import name
from django.urls import path

from . import views

app_name = 'locationgameapp'
urlpatterns = [
    path('', views.index, name='index'),

    path('Game/', views.Game, name='Game'),

    path('AddLocations/', views.AddLocations, name='AddLocations'),

    path('Leaderboards', views.Leaderboards, name='Leaderboards')
]
