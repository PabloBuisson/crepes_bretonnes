from django.urls import path, re_path
from . import views

urlpatterns = [
    # Une string vide indique la racine
    path('', views.liste, name='url_liste'),
    path('nouveau', views.URLCreate.as_view(), name='url_nouveau'),
    # (?P<code>\w{6}) capturera 6 caractères alphanumériques.
    re_path(r'^(?P<code>\w{6})/$', views.redirection, name='url_redirection'),
]
