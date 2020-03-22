from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView  # L'import a changé
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('contact/', views.contact, name='contact'),
    path('nouveau-contact/', views.nouveau_contact, name='nouveau-contact'),
    path('voir_contacts/', views.voir_contacts, name='liste-contacts'),
    url(r'^faq', TemplateView.as_view(template_name='blog/faq.html')), # ++
]
