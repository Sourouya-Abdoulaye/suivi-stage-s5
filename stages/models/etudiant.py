from django.db import models
from .personne import Personne
from .competence import Competence



class Etudiant(Personne):
    matricule = models.CharField(max_length=100)
    promotion = models.PositiveIntegerField()
    competences = models.ManyToManyField(Competence, related_name="etudiants")
   

    class Meta(Personne.Meta):

        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants"
