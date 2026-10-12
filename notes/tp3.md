# Réponses

## a. Où placer la feuille de style, et pourquoi ?

Placez le fichier dans `stages/static/stages/style.css`.

Django pourra ainsi le retrouver parmi les fichiers statiques de l’application. Le sous-dossier `stages` évite aussi les conflits avec des fichiers portant le même nom dans d’autres applications.

## b. Pourquoi utiliser `{% static 'stages/style.css' %}` ?

La balise `{% static %}` demande à Django de générer l’adresse correcte du fichier statique. En production, cette adresse peut différer du chemin utilisé en développement : les fichiers peuvent être servis depuis un autre domaine ou un préfixe particulier.

Écrire directement `/static/stages/style.css` risquerait de ne plus fonctionner si la configuration change.



## 4.1 — La mesure
J’ai lancé la mesure dans le shell Django avec les six offres du peuplement :  

```python  
from django.db import connection, reset_queries   
from stages.models import Offre  

reset_queries()  

for offre in Offre.objects.all():   
        offre.entreprise.nom  
        list(offre.competences.all())    

len(connection.queries)  
### Résultat :
13
```

### a. Nombre de requêtes
La mesure donne 13 requêtes pour 6 offres :  

1 requête pour récupérer la liste des offres ;  
6 requêtes pour récupérer les entreprises associées ;    
6 requêtes pour récupérer les compétences associées.  
La formule est donc 1 + 2N, où N est le nombre d’offres. C’est un problème de type N+1 : après la requête initiale, deux requêtes supplémentaires sont exécutées pour chaque offre.

### b. Dernière requête
connection.queries[-1] contient un dictionnaire avec notamment le SQL exécuté et sa durée, sous les clés (sql et time).

La dernière requête récupère les compétences associées à la dernière offre parcourue. Elle passe par la table de relation plusieurs-à-plusieurs entre les offres et les compétences. Cela montre que l’ORM exécute les requêtes au moment où les données sont demandées : list(offre.competences.all()) évalue le QuerySet et déclenche la requête SQL.

### c. Avec 200 et 2 000 offres
`En utilisant la même boucle :`

Pour 200 offres : 1 + 2 × 200 = 401 requêtes.  
Pour 2 000 offres : 1 + 2 × 2 000 = 4 001 requêtes.  
Le nombre de requêtes augmente donc avec le nombre d’offres. Pour réduire ce coût, on peut charger l’entreprise avec select_related("entreprise") et les compétences avec prefetch_related("competences").



## 4.2 La correction
Mesures réalisées avec **6 offres** en base. La boucle consulte, pour chaque offre, son entreprise et ses compétences.

| Mesure | Requêtes |
|---|---:|
| Sans optimisation | 13 |
| Avec `select_related("entreprise")` | 7 |
| Avec `select_related("entreprise")` et `prefetch_related("competences")` | 3 |

## Requête utilisée pour chaque mesure

### Sans optimisation

```
python
offres = Offre.objects.all()
```

### Avec select_related
```
python

offres = Offre.objects.select_related("entreprise")
```

### Avec les deux optimisations
```
python

offres = Offre.objects.select_related(
    "entreprise"
).prefetch_related("competences")
```

### Pour chaque mesure, j’ai remis le compteur à zéro avant la boucle :

```
python

from django.db import connection, reset_queries
from stages.models import Offre

reset_queries()

for offre in offres:
    offre.entreprise.nom
    list(offre.competences.all())

len(connection.queries)
```

## d. Pourquoi deux outils différents ?
entreprise est une relation ForeignKey : chaque offre est associée à une seule entreprise. select_related("entreprise") récupère l’offre et son entreprise dans la même requête SQL, à l’aide d’une jointure.

competences est une relation ManyToMany : une offre peut avoir plusieurs compétences, et une compétence peut être liée à plusieurs offres. prefetch_related("competences") récupère les compétences dans une requête séparée, puis Django les associe aux offres en mémoire.

Les deux outils répondent donc à des types de relations différents : select_related pour les relations vers un seul objet, et prefetch_related pour les relations qui peuvent renvoyer plusieurs objets.

## e. Pourquoi prefetch_related est-il un gain ?
prefetch_related exécute bien une requête supplémentaire pour récupérer les compétences. Mais cette requête récupère en une fois les compétences de toutes les offres, au lieu d’exécuter une requête séparée pour chacune.

Avec 6 offres, les requêtes liées aux compétences passent ainsi de 6 à 1. Le total passe de 7 à 3 requêtes lorsque prefetch_related est ajouté à select_related. Le gain devient encore plus important quand le nombre d’offres augmente.



## 4.3 — Le piège

J’ai mesuré la page de détail d’une entreprise en comptant la requête qui récupère l’entreprise et celle qui récupère sa liste d’offres.

### f. La page souffre-t-elle du même défaut ?

Non, pas dans cette page. L’entreprise est récupérée par une requête, puis toutes ses offres sont récupérées ensemble par une autre requête. Le nombre de requêtes reste donc **2**, que l’entreprise ait deux offres ou davantage.

La page n’a pas le problème N+1, car elle ne fait pas une requête séparée pour chaque offre. Les champs affichés — titre, dates et nombre de places — appartiennent directement aux offres.

Ajouter `prefetch_related("offres")` à la requête de l’entreprise ne réduit pas le nombre de requêtes ici : Django doit quand même faire une requête pour charger les offres.  

La situation changerait si la page affichais, pour chaque offre, ses compétences. Dans ce cas, on pourrait précharger les deux relations :

```python
entreprise = get_object_or_404(
    Entreprise.objects.prefetch_related("offres_competences"),
    pk=pk,
)
```

## 5. Une panne à diagnostiquer

J’ai changé une lettre dans le nom d’une route utilisé par une balise `{% url %}`, puis j’ai rechargé la page.

### a. Nom et moment de l’erreur

Django affiche une erreur **`NoReverseMatch`**. Elle survient **au chargement de la page**, lorsque Django rend le gabarit et tente de convertir le nom de la route en URL.

Elle ne survient pas au démarrage du serveur ni au clic sur le lien : la balise `{% url %}` est évaluée avant que le navigateur affiche la page.

### b. Comparaison avec une adresse écrite en dur

Si l’adresse avait été écrite en dur, Django n’aurait pas signalé d’erreur lors du rendu du gabarit. La page aurait probablement chargé, puis le clic sur le lien aurait mené à une erreur 404 ou à une mauvaise page.

Je préfère découvrir l’erreur `NoReverseMatch` au chargement de la page : elle révèle immédiatement que le nom de route est incorrect, plutôt que de laisser un lien cassé dans l’application.



## Restitution 
### 1. Pourquoi 50 offres déclenchent-elles 101 requêtes ?

La première requête récupère les 50 offres. Ensuite, pour chaque offre, le programme récupère séparément son entreprise et ses compétences : 50 requêtes pour les entreprises et 50 pour les compétences. Au total, cela fait 1 + 50 + 50 = 101 requêtes. Le problème vient des requêtes répétées dans la boucle ; on peut le réduire en chargeant les relations en groupe.

### 2. Quand choisir select_related ou prefetch_related ?

J’utilise select_related quand chaque objet est lié à un seul autre objet par une clé étrangère ou une relation un-à-un. Dans mon projet, une offre a une seule entreprise :

```
python
Offre.objects.select_related("entreprise")
```

J’utilise prefetch_related quand une relation peut renvoyer plusieurs objets, comme une relation plusieurs-à-plusieurs ou la relation inverse. Dans mon projet, une offre peut demander plusieurs compétences :

```
python
Offre.objects.prefetch_related("competences")
```

  
Note: Mr je n'est pas nommer le fichier (mesure.md) car je voulais garder l'ordre de mes tp dans le dossier notes/  
Merci