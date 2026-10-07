# Tp2 Django
## 1- Models
### a- Django répond : No changes detected (Aucun changement détecté).

Cela apprend deux choses essentielles :

Identification du modèle : Django identifie un modèle par son app_label (le nom de l'application) et son nom de classe (ex. Article), pas par le fichier Python où il est défini. Déplacer ou renommer le fichier ne change rien tant que la classe garde le même nom dans la même app.

Une migration : est un fichier Python déclaratif qui enregistre l'état du schéma de base de données.  Elle ne référence jamais le chemin du fichier source — elle décrit uniquement ce que la base doit être. 



## 2- Analyse du parole de la responsable des stages  et identification du besoin


### 1. Tables

#### `stages_competence`

- `id` — integer, PK, AUTOINCREMENT
- `libelle` — varchar(100), NOT NULL, UNIQUE

---

#### `stages_entreprise`

- `id` — integer, PK, AUTOINCREMENT
- `nom` — varchar(100), NOT NULL
- `ville` — varchar(80), NOT NULL
- `secteur` — varchar(80), NOT NULL
- `contact` — varchar(254), NOT NULL

**Contraintes :**
- `UNIQUE (nom, ville)`

---

#### `stages_enseignantreferent`

- `id` — integer, PK, AUTOINCREMENT
- `nom` — varchar(100), NOT NULL
- `prenom` — varchar(100), NOT NULL
- `sexe` — varchar, NOT NULL
- `date_naissance` — date, NOT NULL
- `email` — varchar(120), NOT NULL

---

#### `stages_tuteurentreprise`

- `id` — integer, PK, AUTOINCREMENT
- `nom` — varchar(100), NOT NULL
- `prenom` — varchar(100), NOT NULL
- `sexe` — varchar, NOT NULL
- `date_naissance` — date, NOT NULL
- `email` — varchar(120), NOT NULL
- `entreprise_id` — bigint, NOT NULL, FK → `stages_entreprise(id)`

---

#### `stages_etudiant`

- `id` — integer, PK, AUTOINCREMENT
- `nom` — varchar(100), NOT NULL
- `prenom` — varchar(100), NOT NULL
- `sexe` — varchar, NOT NULL
- `date_naissance` — date, NOT NULL
- `email` — varchar(120), NOT NULL
- `matricule` — varchar(100), NOT NULL
- `promotion` — integer unsigned, NOT NULL, CHECK ≥ 0

---

#### `stages_offre`

- `id` — integer, PK, AUTOINCREMENT
- `titre` — varchar(100), NOT NULL
- `Description` — text, NOT NULL
- `Date_debut` — date, NOT NULL
- `Date_fin` — date, NOT NULL
- `Nb_places` — integer, NOT NULL
- `entreprise_id` — bigint, NOT NULL, FK → `stages_entreprise(id)`

---

#### `stages_candidature`

- `id` — integer, PK, AUTOINCREMENT
- `statut` — varchar(20), NOT NULL
- `date_depot` — date, NOT NULL
- `etudiant_id` — bigint, NULL, FK → `stages_etudiant(id)`
- `offre_id` — bigint, NULL, FK → `stages_offre(id)`

**Contraintes :**
- `UNIQUE (etudiant_id, offre_id)`

---

#### `stages_stage`

- `id` — integer, PK, AUTOINCREMENT
- `sujet` — varchar(100), NOT NULL
- `enseignantReferent_id` — bigint, NOT NULL, FK → `stages_enseignantreferent(id)`
- `tuteurEntreprise_id` — bigint, NOT NULL, FK → `stages_tuteurentreprise(id)`

