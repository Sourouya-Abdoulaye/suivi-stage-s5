from ..models.candidature import Candidature
from ..models.offre import Offre
from ..models.etudiant import Etudiant
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from ..form import CandidatureForm, TraitementCandidatureForm


def traiter_candidature(request: HttpRequest, candidature_id):
    candidature = get_object_or_404(Candidature, pk=candidature_id)

    if request.method == "POST":
        form = TraitementCandidatureForm(request.POST, instance=candidature)
        if form.is_valid:
            # candidature.statut = "en_attente"
            form.save()
            # return render(
            #     request,
            #     "stages/detail_offre.html",
            #     {"offre": candidature.offre},
            # )

    print(candidature.offre.id)
    return redirect("stages:detail_offre", id=candidature.offre.id)


def detail_candidature(request: HttpRequest, candidature_id):
    candidature = get_object_or_404(Candidature, pk=candidature_id)
    return render(
        request,
        "stages/detail_candidature.html",
        {"candidature": candidature},
    )


def candidature(request: HttpRequest, offre_id, etudiant_id):
    offre = get_object_or_404(Offre, pk=offre_id)
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)

    if request.method == "POST":
        candidature_form = CandidatureForm(request.POST)

        if candidature_form.is_valid:
            existing = Candidature.objects.filter(
                etudiant=etudiant, offre=offre
            ).first()

            if existing:
                # Option A : rediriger vers la candidature existante
                return redirect("stages:detail_candidature", id=existing.id)
                # Option B : afficher un message d'erreur
                # messages.error(request, "Cet étudiant a déjà postulé à cette offre.")
            else:
                candidature = candidature_form.save(commit=False)
                candidature.etudiant = etudiant
                candidature.offre = offre
                candidature.save()
                return redirect("stages:detail_candidature", id=candidature.id)
    else:
        # objet du form
        form = CandidatureForm()

    print(offre)
    print(etudiant)
    return render(
        request,
        "stages/candidature.html",
        {"offre": offre, "etudiant": etudiant, "form": form},
    )
