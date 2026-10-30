from django.urls import path
from .views import entreprise
from .views import offre
from .views import stage
from .views import candidature

app_name = "stages"
urlpatterns = [
    # offres
    path("", offre.liste_offres, name="liste_offres"),
    path(
        "offres/publier/<int:entreprise_id>/", offre.publier_offre, name="publier_offre"
    ),
    path("offre/<int:pk>/", offre.detail_offre, name="detail_offre"),
    # candidature d'un etudiant
    path(
        "candidatures/<int:offre_id>/<int:etudiant_id>",
        candidature.candidature,
        name="candidature",
    ),
    path(
        "candidatures/<int:candidature_id>",
        candidature.detail_candidature,
        name="detail_candidature",
    ),
    # assepter ou refuser la candidature
    path(
        "traiter_candidatures/<int:candidature_id>",
        candidature.traiter_candidature,
        name="traiter_candidature",
    ),
    path("stages/", stage.liste_stages, name="liste_stages"),
    path("stage/<int:pk>/", stage.detail_stage, name="detail_stage"),
    path("entreprises/", entreprise.liste_entreprises, name="liste_entreprises"),
    path(
        "entreprises/<int:pk>/", entreprise.detail_entreprise, name="detail_entreprise"
    ),
]
