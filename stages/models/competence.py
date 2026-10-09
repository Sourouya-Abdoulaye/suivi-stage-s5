from django.db import models


class Competence(models.Model):
    libelle = models.CharField(max_length=100,unique=True)
    
    class Meta:
        verbose_name="Competence"
        verbose_name_plural="Competences"

    
    def __str__(self):
        return f"{self.libelle}"