# Tp2 Django
## 1- Models
### a- Django répond : No changes detected (Aucun changement détecté).

Cela apprend deux choses essentielles :

Identification du modèle : Django identifie un modèle par son app_label (le nom de l'application) et son nom de classe (ex. Article), pas par le fichier Python où il est défini. Déplacer ou renommer le fichier ne change rien tant que la classe garde le même nom dans la même app.

Une migration : est un fichier Python déclaratif qui enregistre l'état du schéma de base de données.  Elle ne référence jamais le chemin du fichier source — elle décrit uniquement ce que la base doit être. 



## 2- Analyse du parole de la responsable des stages  et identification du besoin

### Models
#### * Entreprise
- Nom  
- Ville  
- Secteur
- Contact

#### * Offfres
- titre
- Description,  
- Date_debut,  
- Date_fin,  
- Nb_places,  
- Competence  

#### * Personne
- nom,  
- prenom,  
- sexe,  
- date_naissance,  
- email,  


#### *  (Etudiant,tuteur_entreprise,enseignant_referent) herite de Personne

#### * Etudiant
- matricule,  
- promotion

### * competence
- Libelle,  

### * candidature
- statut
- date_depot

### * stage
- sujet


### Les constraintes


