from django.db import models
from .etudiant import Etudiant
from .offre import Offre


class Candidature(models.Model):

    STATUS = [
        ("accepte", "ACCEPTE"),
        ("rejeter", "REJETER"),
        ("en attente", "EN_ATTENTE"),
    ]

    statut = models.CharField(choices=STATUS, default=STATUS[2])
    date_depot = models.DateField(auto_now=True)
    etudiant = models.ForeignKey(Etudiant,on_delete=models.SET_NULL,related_name="candidatures",null=True)
    offre = models.ForeignKey(Offre,on_delete=models.SET_NULL,related_name="candidatures",null=True)
    

    class Meta:
        verbose_name = "Competence"
        verbose_name_plural = "Competences"
       