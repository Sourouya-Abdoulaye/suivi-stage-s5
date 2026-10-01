from django.db import models
from .enseignant_referent import EnseignantReferent
from .tuteur_entreprise import TuteurEntreprise
from .etudiant import Etudiant


class Stage(models.Model):
    sujet = models.CharField(max_length=100)
    enseignantReferent = models.ForeignKey(
        EnseignantReferent, on_delete=models.PROTECT, related_name="stages"
    )
    tuteurEntreprise = models.ForeignKey(
        TuteurEntreprise, on_delete=models.PROTECT, related_name="stages"
    )
    etudiants = models.ManyToManyField(Etudiant, related_name="stages")

    class Meta:
        verbose_name = "Stage"
        verbose_name_plural = "Stages"
