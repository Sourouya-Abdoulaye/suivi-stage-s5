from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):

    list_display = ("nom", "ville", "secteur")
    search_fields = ("nom", "ville")


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ("id", "libelle")
    search_fields = ("libelle",)


@admin.register(EnseignantReferent)
class EnseignantReferentAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "prenom", "sexe", "email")
    list_filter = ("sexe",)
    search_fields = ("nom", "prenom", "email")


@admin.register(TuteurEntreprise)
class TuteurEntrepriseAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "prenom", "sexe", "email")
    list_filter = ("sexe",)
    search_fields = ("nom", "prenom", "email")


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ("matricule", "nom", "prenom", "promotion", "email")
    list_filter = ("promotion", "sexe")
    search_fields = ("matricule", "nom", "prenom", "email")
    filter_horizontal = (
        "competences",
    ) 


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ("id", "sujet", "enseignantReferent", "tuteurEntreprise")
    search_fields = ("sujet", "enseignantReferent__nom", "tuteurEntreprise__nom")
    list_filter = ("enseignantReferent", "tuteurEntreprise")


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ("titre", "entreprise", "Date_debut", "Date_fin", "Nb_places")
    list_filter = ("entreprise", "Date_debut")
    search_fields = ("titre", "Description", "entreprise__nom")
    filter_horizontal = ("competences",)


@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ("id", "etudiant", "offre", "statut", "date_depot")
    list_filter = ("statut", "date_depot")
    search_fields = ("etudiant__nom", "etudiant__prenom", "offre__titre")
