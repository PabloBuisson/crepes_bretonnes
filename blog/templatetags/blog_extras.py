from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
def citation(texte):
    """
    Affiche le texte passé en paramètre, encadré de guillemets 
    français doubles et d'espaces insécables.
    """
    res = "&laquo; {} &raquo;".format(escape(texte))
    return mark_safe(res)


@register.filter
def smart_truncate(texte, nb_caracteres=20):
    """
    Coupe la chaîne de caractères jusqu'au nombre de caractères souhaité,
    sans couper la nouvelle chaîne au milieu d'un mot.
    Si la chaîne est plus petite, elle est renvoyée sans points de suspension.
    ---
    Exemple d'utilisation :
    {{ "Bonjour tout le monde, c'est Diego"|smart_truncate:18 }} renvoie
    "Bonjour tout le..."
    """
    # Nous vérifions tout d'abord que l'argument passé est bien un nombre
    try:
        nb_caracteres = int(nb_caracteres)
    except ValueError:
        return texte  # Retour de la chaîne originale sinon

    # Si la chaîne est plus petite que le nombre de caractères maximum voulus,
    # nous renvoyons directement la chaîne telle quelle.
    if len(texte) <= nb_caracteres:
        return texte

    # Sinon, nous coupons au maximum, tout en gardant le caractère suivant
    # pour savoir si nous avons coupé à la fin d'un mot ou en plein milieu
    texte = texte[:nb_caracteres + 1]
    # slice [:nb] = garde tous les éléments, de 0 à nb

    # Nous vérifions d'abord que le dernier caractère n'est pas une espace,
    # autrement, il est inutile d'enlever le dernier mot !
    if texte[-1:] != ' ':
        mots = texte.split(' ')[:-1]
        # enlève le dernier mot du texte.split
        texte = ' '.join(mots)
    else:
        texte = texte[0:-1]
        # garde toutes les lettres sauf la dernière

    return texte + '…'
