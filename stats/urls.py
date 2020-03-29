from django.urls import path
from . import views

urlpatterns = [
    # Une string vide indique la racine
    path('', views.accueil, name='accueil'),
]
