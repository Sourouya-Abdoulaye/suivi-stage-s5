from django.db import models
from .personne import Personne


class TuteurEntreprise(Personne):

    class Meta(Personne.Meta):
        verbose_name = "TuteurEntreprise"
        verbose_name_plural = "TuteursEntreprise"
