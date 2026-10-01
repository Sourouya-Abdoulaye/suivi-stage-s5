from django.db import models
from .etudiant import Etudiant
from .offre import Offre


class Candidature(models.Model):
    STATUS = [
        ("accepte", "ACCEPTE"),
        ("rejeter", "REJETER"),
        ("en_attente", "EN_ATTENTE"),
    ]

    statut = models.CharField(max_length=20, choices=STATUS, default="en_attente")
    date_depot = models.DateField(auto_now=True)
    etudiant = models.ForeignKey(
        Etudiant, on_delete=models.SET_NULL, related_name="candidatures", null=True
    )
    offre = models.ForeignKey(
        Offre, on_delete=models.SET_NULL, related_name="candidatures", null=True
    )

    class Meta:
        verbose_name = "Candidature"
        verbose_name_plural = "Candidatures"
        constraints = [
            models.UniqueConstraint(
                fields=["etudiant", "offre"],
                name="unique_etudiant_offre",
            )
        ]

    def __str__(self):
        return f"{self.etudiant} → {self.offre} ({self.statut})"   