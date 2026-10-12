from django.shortcuts import get_object_or_404, render
from ..models.stage import Stage


def liste_stages(request):
    stages = (
        Stage.objects
        .select_related("tuteurEntreprise")
        .select_related("enseignantReferent")
        .prefetch_related("etudiants")
    )
    return render(
        request,
        "stages/liste_stages.html",
        {"stages": stages},
    )


def detail_stage(request, pk):
    stage = get_object_or_404(Stage, pk=pk)
    return render(
        request,
        "stages/detail_stage.html",
        {"stage": stage},
    )
