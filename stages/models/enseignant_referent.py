from django.db import models
from .personne import Personne


class EnseignantReferent(Personne):

    class Meta(Personne.Meta):
        verbose_name = "EnseignantReferent"
        verbose_name_plural = "EnseignantsReferent"
        
        
