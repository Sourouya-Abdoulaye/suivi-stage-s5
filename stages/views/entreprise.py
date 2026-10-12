from django.shortcuts import get_object_or_404, render
from ..models.entreprise import Entreprise

# Create your views here.
def liste_entreprises(request):
    return render(
        request,
        "stages/liste_entreprises.html",
        {"entreprises": Entreprise.objects.all()},
    )


def detail_entreprise(request, pk):
    entreprise = get_object_or_404(Entreprise,pk=pk)

    # if entreprise:
    #     print(entreprise)

    return render(
        request,
        "stages/detail_entreprise.html",
        {"entreprise": entreprise},
    )

