from unicodedata import name
from django.urls import path

from . import views

app_name = 'locationgameapp'
urlpatterns = [
    path('', views.index, name='index'),

    path('homePage/', views.homePage, name='homePage'),

    path('Game/', views.Game, name='Game'),

    path('Settings/', views.Settings, name='Settings'),

    path('Leaderboards', views.Leaderboards, name='Leaderboards')
    ]