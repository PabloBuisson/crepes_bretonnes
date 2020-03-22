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

    def clean(self):
        cleaned_data = super(ContactForm, self).clean() # appelle la méthode clean héritée de Form
        # Appeler la méthode mère permet au framework de vérifier tous les champs comme d’habitude 
        # pour s’assurer que ceux-ci sont corrects
        # La méthode mère clean va également renvoyer un dictionnaire avec toutes les données valides
        sujet = cleaned_data.get('sujet') # renvoie la valeur d’une clé si elle existe, et renvoie None sinon
        message = cleaned_data.get('message')

        if sujet and message:  # Est-ce que sujet et message sont valides ?
            if "pizza" in sujet and "pizza" in message:
                # si les deux champs contiennent le mot « pizza »,
                # nous ne renvoyons plus une exception, mais nous ajoutons une erreur
                # l’appel à cette méthode a pour effet de supprimer le message des données "valide" 
                # et donc d’empêcher toute nouvelle validation de ce champ
                self.add_error("message", 
                    "Vous parlez déjà de pizzas dans le sujet, "
                    "n'en parlez plus dans le message !"
                )
                # on peut également spécifier comme deuxième paramètre de la méthode
                # une instance de forms.ValidationError, comme utilisé précédemment
        return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK


class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()
