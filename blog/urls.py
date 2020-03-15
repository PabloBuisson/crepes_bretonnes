from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
]
