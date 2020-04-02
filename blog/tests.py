from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Article

# regroupe tous les tests concernant le modèle Article
class ArticleTests(TestCase):
    # chaque méthode de test commence par test_
    def test_est_recent_avec_futur_article(self):
        """
        Vérifie si la méthode est_recent d'un Article ne
        renvoie pas True si l'Article a sa date de publication
        dans le futur.
        """
        # crée un article censé être publié dans 20 jours 
        # et vérifie si sa méthode est_recent renvoie True ou False (espéré)
        futur_article = Article(date=timezone.now() + timedelta(days=20))
        # Il n'y a pas besoin de remplir tous les champs, ni de sauvegarder
        self.assertEqual(futur_article.est_recent(), False)
