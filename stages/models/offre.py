from django.db import models
from .competence import Competence
from .entreprise import Entreprise


class Offre(models.Model):
    titre = models.CharField(max_length=100)
    Description = models.TextField(max_length=300)
    Date_debut = models.DateField()
    Date_fin = models.DateField()
    Nb_places = models.IntegerField()

    competences = models.ManyToManyField(Competence, related_name="offres")
    entreprise = models.ForeignKey(
        Entreprise, related_name="offres", on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "Offre"
        verbose_name_plural = "Offres"

    def __str__(self):
        return f"{self.titre} - {self.Date_debut}"