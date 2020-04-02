from django.db import models
from django.utils import timezone

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)  # ++

    class Meta:
        ordering = ['date']

    def est_recent(self):
        """ Retourne True si l'article a été publié dans
            les 30 derniers jours """
        return (timezone.now() - self.date).days < 30

    def __str__(self):
        return self.titre


class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/") # contiendra une image

    def __str__(self):
        return self.nom
