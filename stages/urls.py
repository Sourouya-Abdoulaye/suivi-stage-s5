from django.urls import path
from .views import entreprise
from .views import offre
from .views import stage

app_name = "stages"
urlpatterns = [
    path('', offre.liste_offres, name="liste_offres"),
    path(
            "offre/<int:pk>/", offre.detail_offre, name="detail_offre"
        ),
    
    path('stages/', stage.liste_stages, name="liste_stages"),
        path(
                "stage/<int:pk>/", stage.detail_stage, name="detail_stage"
            ),
    path("entreprises/", entreprise.liste_entreprises, name="liste_entreprises"),
    path(
        "entreprises/<int:pk>/", entreprise.detail_entreprise, name="detail_entreprise"
    ),
]
