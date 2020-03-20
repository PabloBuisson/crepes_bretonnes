from django import forms

class ContactForm(forms.Form):
    # enregistre toujours du texte, remplace TextField
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    # les widgets * transforment le code HTML pour le rendre plus adapté à la situation actuelle
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    # label permet de modifier le nom de la boîte de saisie
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.",
                                required=False)  # case à cocher
    # help_text permet d’ajouter un petit texte d’aide concernant le champ
