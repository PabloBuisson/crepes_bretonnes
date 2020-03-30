from django.urls import path
from . import views

urlpatterns = [
    path('connexion', views.connexion, name='connexion')
]
