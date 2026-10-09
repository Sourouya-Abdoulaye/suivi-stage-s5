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



## Partie 6 — Ce que la base accepte

### a. Résultats

| # | Test | Résultat |
|---|------|----------|
| 1 | `Date_debut="2028-12-01"`, `Date_fin="2027-04-01"` | **Acceptée** — l'offre est créée sans erreur |
| 2 | `titre=""` | **Acceptée** — l'offre est créée sans erreur |
| 3 | Deux candidatures identiques (même étudiant + même offre) | **Refusée** — `IntegrityError` |

### b. Le problème commun (cas 1 et 2)

Les deux relèvent de l'**absence de contrainte métier** dans le schéma SQL :

- **Cas 1** : aucun `CHECK (Date_fin >= Date_debut)` dans `stages_offre` → la base ne peut pas détecter l'incohérence.
- **Cas 2** : `titre` est `NOT NULL`, mais `""` n'est pas NULL → la base l'accepte. Aucun `CHECK (length(titre) > 0)`.

**Qui aurait dû refuser ?** Le **modèle Django** (via `clean()` ou `CheckConstraint`) ou le **formulaire** (`blank=False`). La base ne connaît pas ces règles.

> Le cas 3, lui, est refusé par la base car `CONSTRAINT "unique_etudiant_offre" UNIQUE ("etudiant_id", "offre_id")` est **dans le schéma SQL**.

---

## Restitution

### 1. Comportement à la suppression (Offre ↔ Candidature)

Dans le schéma, `offre_id` dans `stages_candidature` est **NULL** → `on_delete=SET_NULL`.

> « Si on supprime une offre, la candidature reste mais sans offre, pour garder la trace que l'étudiant a bien postulé à quelque chose. »

Si on avait choisi `CASCADE` : supprimer une offre effacerait **toutes** les candidatures associées, faisant perdre l'historique des postulants.

### 2. Situation concrète d'incohérence

Un développeur exécute `DELETE FROM stages_offre WHERE id = 5` directement en SQLite (via `sqlite3` ou un outil d'admin) au lieu de passer par Django. Les `on_delete=SET_NULL` **ne s'exécutent pas** car ce sont des règles appliquées par Django en Python, pas par la base. Résultat : les candidatures liées conservent `offre_id = 5` → **référence orpheline** en base.

### 3. Pourquoi la base a refusé une et accepté les deux autres

- **Cas 3 (refusé)** : la contrainte `UNIQUE ("etudiant_id", "offre_id")` est **structurelle**, écrite dans le schéma SQL. La base la connaît et l'applique automatiquement.
- **Cas 1 et 2 (acceptés)** : ce sont des **règles métier** (cohérence des dates, titre non vide) qui n'existent pas en tant que `CHECK` dans le schéma. La base ne refuse que ce qu'elle sait exprimer.

**Différence** : la contrainte d'unicité est une règle **structurelle** (la base la gère nativement), tandis que les autres sont des règles **métier** (à implémenter dans le modèle Django).   