from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from secret.forms import ConnexionForm

def accueil(request):
    return render(request, 'secret/accueil.html', locals())

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # Nous vérifions si les données sont correctes
            user = authenticate(username=username, password=password)
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else:  # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'secret/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))
    # reverse crée une directive semblable à la balise de gabarit url
    # {% url 'some-url-name' arg1=v1 arg2=v2 %}
