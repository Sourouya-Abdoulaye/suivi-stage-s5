from django.shortcuts import get_object_or_404, redirect, render
from stages.form import OffreForm
from ..models.offre import Offre, Competence, Entreprise
from django.http import HttpRequest, HttpResponse


# Create your views here.
def liste_offres(request):
    offres = Offre.objects.select_related("entreprise").prefetch_related("competences")
    return render(
        request,
        "stages/liste_offres.html",
        {"offres": offres},
    )


def detail_offre(request, pk):
    offre = Offre.objects.prefetch_related("candidatures").get(pk=pk)

    candidatures = offre.candidatures.all()

    return render(
        request,
        "stages/detail_offre.html",
        {"offre": offre,"candidatures":candidatures},
    )


def publier_offre(request: HttpRequest, entreprise_id: int) -> HttpResponse:
    entreprise = get_object_or_404(Entreprise, pk=entreprise_id)
    competences = Competence.objects.all()
    
    print("=============================")
    print(request.POST)
    print("=============================")

    if request.method == "POST":
        form = OffreForm(request.POST)
        
        if form.is_valid():
            offre = form.save(commit=False)
            offre.entreprise=entreprise
            offre.save()
            form.save_m2m()
            
            return redirect("stages:detail_offre",offre.pk)
        
        # offre = Offre.objects.create(
        #     titre=request.POST["titre"],
        #     Description=request.POST["description"],
        #     Date_debut=request.POST["date_debut"],
        #     Date_fin=request.POST["date_fin"],
        #     Nb_places=request.POST["nb_places"],
        #     entreprise=entreprise,
        # )

        # return HttpResponse("Offre publiée")
    
    # pour get
    form = OffreForm()
    return render(
        request,
        "stages/publier_offre.html",
        {"entreprise": entreprise, "competences": competences,"form":form},
    )
