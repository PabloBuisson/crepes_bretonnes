from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('contact/', views.contact, name='contact'),
    path('nouveau-contact/', views.nouveau_contact, name='nouveau-contact'),
    path('voir_contacts/', views.voir_contacts, name='liste-contacts'),
    url(r'^faq$', views.FAQView.as_view()),
    # Nous demandons la vue correspondant à la classe FAQView
]
