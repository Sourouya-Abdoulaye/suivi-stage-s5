from django.db import models
from .enseignant_referent import EnseignantReferent
from .tuteur_entreprise import TuteurEntreprise


class Stage(models.Model):
    sujet = models.CharField(max_length=100)
    enseignantReferent = models.ForeignKey(EnseignantReferent,on_delete=models.PROTECT,related_name="stages")
    tuteurEntreprise = models.ForeignKey(TuteurEntreprise,on_delete=models.PROTECT,related_name="stages")
    
    class Meta:
        verbose_name="Stage"
        verbose_name_plural="Stages"
        
       