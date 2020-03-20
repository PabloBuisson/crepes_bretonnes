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
                raise forms.ValidationError(
                    "Vous parlez de pizzas dans le sujet ET le message ? Non mais ho !"
                )

        return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK
