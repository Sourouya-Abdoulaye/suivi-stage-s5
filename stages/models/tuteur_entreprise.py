from django.db import models
from .personne import Personne
from .entreprise import Entreprise


class TuteurEntreprise(Personne):
    entreprise = models.ForeignKey(
        Entreprise, on_delete=models.CASCADE, related_name="tuteur_entreprise",default=1
    )

    class Meta(Personne.Meta):
        verbose_name = "TuteurEntreprise"
        verbose_name_plural = "TuteursEntreprise"
