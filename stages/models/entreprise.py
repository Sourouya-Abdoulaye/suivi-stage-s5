from django.db import models

# Create your models here.


# creation de la table migration
class Entreprise(models.Model):

    SECTEURS = [
        ("technologie", 'Technologie'),
        ("sante","Sante",),
        ("commerce", "Commerce"),
        ]

    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=80)
    secteur = models.CharField(max_length=80, choices=SECTEURS)
    contact = models.EmailField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["nom", "ville"], name="unique_entreprise_nom_ville"
            )
        ]
        ordering = ["nom"]
        verbose_name = "entreprise"
        verbose_name_plural = "entreprises"

    def __str__(self):
        return f"{self.nom} ({self.ville})"
