'''URL routing'''

from django.urls import path

from . import views

app_name = 'locationgameapp'

urlpatterns = [
    path('', views.index, name='index'),

    path('Game/', views.Game, name='Game'),

    path('Leaderboards', views.Leaderboards, name='Leaderboards')
    ]
