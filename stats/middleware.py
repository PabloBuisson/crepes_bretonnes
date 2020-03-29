from django.db.models import F
from .models import Page

def stats_middleware(get_response):
    def middleware(request):
        # Avant chaque exécution de la vue, on incrémente
        # le nombre de page vues à chaque appel de vues
        try:
            # Le compteur lié à la page est récupéré et incrémenté
            p = Page.objects.get(url=request.path)
            p.nb_visites = F('nb_visites') + 1
            # équivalent de UPDATE stats_page SET nb_visites=nb_visites+1
            p.save()
        except Page.DoesNotExist:
            # Un nouveau compteur à 1 par défaut est créé
            p = Page.objects.create(url=request.path)

        # Appel de la vue Django
        response = get_response(request)

        # Une fois la vue exécutée, on ajoute à la fin le nombre
        # de vues de la page
        response.content += bytes(
            "Cette page a été vue {0} fois.".format(p.nb_visites),
            "utf8"
        )
        # Et on retourne le résultat
        return response

    return middleware
