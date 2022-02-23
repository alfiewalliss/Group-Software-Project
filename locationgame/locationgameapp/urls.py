from django.urls import path

from . import views

app_name = 'locationgameapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('signUp/', views.signUp, name='signUp'),
    path('login/', views.login, name='login'),
]