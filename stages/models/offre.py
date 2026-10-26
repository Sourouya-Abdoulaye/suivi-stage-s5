from django.db import models
from .competence import Competence
from .entreprise import Entreprise

from django.core.exceptions import ValidationError


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
    
    def clean(self):
       if self.Date_debut >= self.Date_fin:
           
            raise ValidationError(
               {
                   "Date_debut":"la date debut est plus grand que date de fin",
                    "Date_fin":" la date de fin est plus petit que date de debut"
               }
           )
           

    class Meta:
        verbose_name = "Offre"
        verbose_name_plural = "Offres"

    def __str__(self):
        return f"{self.titre} - {self.Date_debut}"