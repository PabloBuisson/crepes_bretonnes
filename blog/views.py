from .forms import ContactForm, NouveauContactForm
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Article, Contact, Categorie
from django.views.generic import TemplateView, ListView, DetailView # ++

# fonction remplacée par LireArticles()
# def accueil(request):
#    """ Afficher tous les articles de notre blog """
#    articles = Article.objects.all() # Nous sélectionnons tous nos articles
#    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

# fonction remplacée par LireArticle()
# def lire(request, id, slug):
#    """ Afficher un article complet """
#    article = get_object_or_404(Article, id=id, slug=slug)
#    return render(request, 'blog/lire.html', {'article':article})

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())


def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    # tous tous les fichiers sélectionnés sont envoyés dans
    # le dictionnaire request.FILES
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'blog/nouveau-contact.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })


def voir_contacts(request):
    return render(
        request,
        'blog/voir_contacts.html',
        {'contacts': Contact.objects.all()}
    )


class ListeArticles(ListView):
    model = Article
    context_object_name = "derniers_articles"
    template_name = "blog/accueil.html"
    paginate_by = 5 # afficher que 5 articles par page
    queryset = Article.objects.filter(categorie__id=1)
    # filtre les articles de catégorie 1
    # ci-dessous, filtre les articles par catégorie, automatiquement
    # remplace l'attribut queryset
    # def get_queryset(self):
    #   return Article.objects.filter(categorie__id=self.kwargs['id'])
    # (!) demande un path=('<int:id>/', ect.) pour marcher

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(ListeArticles, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories, sans filtre particulier
        context['categories'] = Categorie.objects.all()
        return context


class LireArticle(DetailView):
    context_object_name = "article"
    model = Article
    template_name = "blog/lire.html"
