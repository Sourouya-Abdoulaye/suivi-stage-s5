from django import forms
from .models.offre import Offre
from .models.candidature import Candidature


class OffreForm(forms.ModelForm):

    class Meta:
        model = Offre
        fields = [
            "titre",
            "Description",
            "Date_debut",
            "Date_fin",
            "Nb_places",
            "competences",
        ]


class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ["date_depot"]
        # "date_depot",

class TraitementCandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ["statut"]   