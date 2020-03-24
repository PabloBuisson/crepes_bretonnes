from django.urls import path
from django.views.generic import TemplateView, ListView  # ++
from . import views
from .models import Article # ++

urlpatterns = [
    # Nous allons réécrire l'URL de l'accueil
    path('', views.ListeArticles.as_view(), name="blog_liste"),
    # récupérer les articles par catégories
    path('categorie/<int:id>', views.ListeArticles.as_view(),
            name='blog_categorie'),

    # path('', views.accueil, name='accueil'),
    # path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('article/<int:pk>-<slug:slug>',
         views.LireArticle.as_view(), name='blog_lire'),
    path('contact/', views.contact, name='contact'),
    path('nouveau-contact/', views.nouveau_contact, name='nouveau-contact'),
    path('voir_contacts/', views.voir_contacts, name='liste-contacts'),
    path('faq', TemplateView.as_view(
        template_name='blog/faq.html')),
]
