from django import forms
from .models.offre import Offre


class OffreForm(forms.ModelForm):
    


    class Meta:
        model = Offre
        fields = [
            "titre",
            "Description",
            "Date_debut",
            "Date_fin",
            "Nb_places",
            "competences"
        ]
