from stages.models import (
    Competence,
    Entreprise,
    EnseignantReferent,
    TuteurEntreprise,
    Etudiant,
    Offre,
    Stage,
    Candidature,
)

# Compétences (5) 
c1, _ = Competence.objects.get_or_create(libelle="Python")
c2, _ = Competence.objects.get_or_create(libelle="Django")
c3, _ = Competence.objects.get_or_create(libelle="SQL")
c4, _ = Competence.objects.get_or_create(libelle="JavaScript")
c5, _ = Competence.objects.get_or_create(libelle="React")

# Entreprises (3, dont 2 à Sokodé) 
e1, _ = Entreprise.objects.get_or_create(
    nom="Sokotech", ville="Sokodé", secteur="IT", contact="contact@sokotech.com"
)
e2, _ = Entreprise.objects.get_or_create(
    nom="DataPro", ville="Sokodé", secteur="Data", contact="contact@datapro.com"
)
e3, _ = Entreprise.objects.get_or_create(
    nom="WebDev Lomé", ville="Lomé", secteur="Web", contact="contact@webdev.com"
)

# Enseignants Référents (2) 
er1, _ = EnseignantReferent.objects.get_or_create(
    nom="Koffi",
    prenom="Jean",
    sexe="M",
    date_naissance="1985-03-15",
    email="koffi@univ.com",
)
er2, _ = EnseignantReferent.objects.get_or_create(
    nom="Mensah",
    prenom="Awa",
    sexe="F",
    date_naissance="1988-07-22",
    email="mensah@univ.com",
)

# Tuteurs Entreprise (2) 
t1, _ = TuteurEntreprise.objects.get_or_create(
    nom="Agbeko",
    prenom="Kossi",
    sexe="M",
    date_naissance="1990-01-10",
    email="agbeko@sokotech.com",
    entreprise=e1,
)
t2, _ = TuteurEntreprise.objects.get_or_create(
    nom="Sossou",
    prenom="Afi",
    sexe="F",
    date_naissance="1992-06-20",
    email="sossou@datapro.com",
    entreprise=e2,
)

# Étudiants (5) avec compétences 
et1, _ = Etudiant.objects.get_or_create(
    nom="Abdoulaye",
    prenom="Malik",
    sexe="M",
    date_naissance="2001-02-14",
    email="malik@univ.com",
    matricule="S5-001",
    promotion=5,
)
et1.competences.set([c1, c2, c3])

et2, _ = Etudiant.objects.get_or_create(
    nom="Djossa",
    prenom="Clarisse",
    sexe="F",
    date_naissance="2000-11-05",
    email="clarisse@univ.com",
    matricule="S5-002",
    promotion=5,
)
et2.competences.set([c1, c4, c5])

et3, _ = Etudiant.objects.get_or_create(
    nom="Tchalla",
    prenom="Yao",
    sexe="M",
    date_naissance="2001-08-30",
    email="yao@univ.com",
    matricule="S5-003",
    promotion=5,
)
et3.competences.set([c1, c2, c4])

et4, _ = Etudiant.objects.get_or_create(
    nom="Kodjo",
    prenom="Sena",
    sexe="F",
    date_naissance="2002-04-18",
    email="sena@univ.com",
    matricule="S5-004",
    promotion=5,
)
et4.competences.set([c3, c4])

et5, _ = Etudiant.objects.get_or_create(
    nom="Ameglin",
    prenom="Kokou",
    sexe="M",
    date_naissance="2001-12-01",
    email="kokou@univ.com",
    matricule="S5-005",
    promotion=5,
)
et5.competences.set([c1, c2, c5])

# Offres (3) avec compétences 
o1, _ = Offre.objects.get_or_create(
    titre="Développeur Django Junior",
    Description="Développer des applications web avec Django",
    Date_debut="2026-11-01",
    Date_fin="2027-02-28",
    Nb_places=2,
    entreprise=e1,
)
o1.competences.set([c1, c2, c3])

o2, _ = Offre.objects.get_or_create(
    titre="Data Analyst Junior",
    Description="Analyser et visualiser des données",
    Date_debut="2026-11-15",
    Date_fin="2027-03-15",
    Nb_places=1,
    entreprise=e2,
)
o2.competences.set([c1, c3])

o3, _ = Offre.objects.get_or_create(
    titre="Développeur Front-end",
    Description="Créer des interfaces React",
    Date_debut="2026-12-01",
    Date_fin="2027-04-01",
    Nb_places=2,
    entreprise=e3,
)
o3.competences.set([c4, c5])

# Candidatures (6, statuts variés) 
Candidature.objects.get_or_create(
    etudiant=et1, offre=o1, defaults={"statut": "retenue", "date_depot": "2026-10-01"}
)
Candidature.objects.get_or_create(
    etudiant=et2, offre=o1, defaults={"statut": "refusée", "date_depot": "2026-10-01"}
)
Candidature.objects.get_or_create(
    etudiant=et3, offre=o2, defaults={"statut": "retenue", "date_depot": "2026-10-02"}
)
Candidature.objects.get_or_create(
    etudiant=et4,
    offre=o3,
    defaults={"statut": "en_attente", "date_depot": "2026-10-03"},
)
Candidature.objects.get_or_create(
    etudiant=et5,
    offre=o1,
    defaults={"statut": "en_attente", "date_depot": "2026-10-04"},
)
Candidature.objects.get_or_create(
    etudiant=et2, offre=o3, defaults={"statut": "refusée", "date_depot": "2026-10-05"}
)

# Stages (2, issus de candidatures retenues) 
# Stage 1 : et1 retenu sur o1 (Sokotech) → tuteur = t1 (Sokotech)
stage1, _ = Stage.objects.get_or_create(
    sujet="Application de gestion des stages",
    enseignantReferent=er1,
    tuteurEntreprise=t1,
)
stage1.etudiants.add(et1)

# Stage 2 : et3 retenu sur o2 (DataPro) → tuteur = t2 (DataPro)
stage2, _ = Stage.objects.get_or_create(
    sujet="Tableau de bord analytique", enseignantReferent=er2, tuteurEntreprise=t2
)
stage2.etudiants.add(et3)

print("Peuplement terminé !")



# les requetes