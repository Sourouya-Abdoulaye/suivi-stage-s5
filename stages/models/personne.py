from django.db import models


class Personne(models.Model):

    SEXE = [("f", "Feminin"), ("m", "Masculin"), ("autre", "Autre")]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(choices=SEXE)
    date_naissance = models.DateField()
    email = models.EmailField(max_length=120)

    class Meta:
        abstract = True
        ordering = ["nom"]

    def __str__(self):
        return f"{self.nom} - {self.prenom}"
