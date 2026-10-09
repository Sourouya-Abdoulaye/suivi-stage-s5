# Les Six requêtes dans le shell 
## 1. les offres des entreprises situées à Sokodé ;
Offre.objects.filter(entreprise__ville='Sokodé')
## 2. les étudiants qui possèdent la compétence « Django » ;
Etudiant.objects.filter(competences__libelle='Django')
## 3. les candidatures d’un étudiant donné, en partant de l’objet étudiant ;
etd=Etudiant.objects.get(id=1)  
etd.candidatures.all()
## 4. le nombre de candidatures retenues, sans charger les candidatures en mémoire ;
Candidature.objects.filter(statut='retenue').count()
## 5. les stages dont l’offre vient d’une entreprise de Sokodé ;
Stage.objects.filter(tuteurEntreprise__entreprise__ville='Sokodé')  
## 6. les offres qui demandent au moins une compétence que possède un étudiant donné.
Offre.objects.filter(competences__in=Etudiant.objects.get(id=1).competences.all())   