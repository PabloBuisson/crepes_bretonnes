from django.shortcuts import render

def accueil(request):
    return render(request, 'stats/accueil.html', locals())
