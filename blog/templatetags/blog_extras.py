from django.template.base import VariableDoesNotExist
from random import randint
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


@register.tag
def random(parser, token):
    """ Tag générant un nombre aléatoire, entre les bornes en arguments """
    try:
        nom_tag, begin, end = token.split_contents()
    except ValueError:
        msg = 'Le tag random doit prendre exactement deux arguments.'
        raise template.TemplateSyntaxError(msg)

    return RandomNode(begin, end)


class RandomNode(template.Node):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def render(self, context):
        not_exist = False

        try:
            begin = template.Variable(self.begin).resolve(context)
            self.begin = int(begin)
        except (VariableDoesNotExist, ValueError):
            not_exist = self.begin
        try:
            end = template.Variable(self.end).resolve(context)
            self.end = int(end)
        except (VariableDoesNotExist, ValueError):
            not_exist = self.end

        if not_exist:
            msg = 'L\'argument "%s" n\'existe pas, ou n\'est pas un entier.' % not_exist
            raise template.TemplateSyntaxError(msg)

        # Nous vérifions si le premier entier est bien inférieur au second
        if self.begin > self.end:
            msg = 'L\'argument "begin" doit obligatoirement être inférieur à l\'argument "end" dans le tag random.'
            raise template.TemplateSyntaxError(msg)

        return str(randint(self.begin, self.end))
