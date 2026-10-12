from stages.models import Entreprise


def test_entreprise_s_affiche_avec_sa_ville(db):
    entreprise = Entreprise.objects.create(
        nom="abdoul",
        ville="sokode",
        secteur="informatique",
        contact="abdoul@gmail.com"
    )
    
    
    assert str(entreprise) == "abdoul (sokode)"