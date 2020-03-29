from datetime import datetime

# récupère la date actuelle
def get_infos(request):
    date_actuelle = datetime.now()
    return {'date_actuelle': date_actuelle}
    # renvoie un/des dictionnaire(s) de données 
    # que le framework intégrera à tous nos templates