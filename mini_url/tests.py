from django.test import TestCase
from django.urls import reverse
from .models import MiniURL

# crée une redirection, l’enregistre et la retourne
def creer_url():
    mini = MiniURL(url="http://foo.bar", code=MiniURL.generer(MiniURL, 6), pseudo="Maxime")
    mini.save()
    return mini


class MiniURLTests(TestCase):
    # va s’assurer que lorsque nous créerons une redirection dans la base de données, 
    # celle-ci sera bien affichée par la vue views.liste
    def test_liste(self):
        """ Vérifie si une URL sauvegardée est bien affichée """
        # crée une redirecton
        mini = creer_url()
        # nous demandons ensuite au client intégré au système de test 
        # d’accéder à la vue liste grâce à la méthode get de self.client
        reponse = self.client.get(reverse('url_liste'))
        # Cette méthode prend une URL, c’est pourquoi 
        # nous utilisons la fonction reverse afin d’obtenir l’URL de la vue spécifiée

        # vérifier que notre vue s’est bien exécutée
        self.assertEqual(reponse.status_code, 200)
        # est-ce que l’URL qui vient d’être créée est bien affichée sur la page ?
        # La méthode renvoie une erreur si la chaîne de caractères n’est pas contenue dans la page
        self.assertContains(reponse, mini.url)
        # est-ce que le QuerySetminis contenant toutes les redirections dans notre vue 
        # (celui que nous avons passé à notre template et qui est accessible depuis reponse.context) 
        # est égal au QuerySet indiqué en deuxième paramètre ?
        self.assertQuerysetEqual(reponse.context['minis'], [repr(mini)])

    def test_nouveau_redirection(self):
        """ Vérifie la redirection d'un ajout d'URL """
        data = {
            'url': 'http://www.djangoproject.com',
            'pseudo': 'Jean Dupont',
        }

        reponse = self.client.post(reverse('url_nouveau'), data)
        self.assertEqual(reponse.status_code, 302)
        # vérifie que la réponse est bien une redirection vers l’URL passée en paramètre
        self.assertRedirects(reponse, reverse('url_liste'))


    def test_nouveau_ajout(self):
        """
        Vérifie si après la redirection l'URL ajoutée est bien dans la liste
        """
        data = {
            'url': 'http://www.crepes-bretonnes.com',
            'pseudo': 'Amateur de crêpes',
        }

        # on force Django à suivre la redirection directement en indiquant follow=True
        reponse = self.client.post(reverse('url_nouveau'), data, follow=True)
        self.assertEqual(reponse.status_code, 200)
        self.assertContains(reponse, data['url'])
