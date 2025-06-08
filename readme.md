# InferenceJDM

## Installation

1. ``python3 -m venv .venv``
2. ``source .venv/bin/activate``
3. ``pip install -r requirement.txt``

## Utilisation
1. ``python3 main.py -B`` -> pour lancer le bot discord
2. ``python3 main.py`` -> pour lancer le programme sur terminal


## Explications
Le programme fonctionne avec seulement 4 fichiers python : 
- Le Main, qui gère le lancement de programme
- Le fichier JDM API qui gère les appels api, le cache des réponses, et permet la facilité des appels via des méthodes puissantes
- Inférence, qui permet à trouver plusieurs types d'inférences et de les trier par ordre de certitude de la relations
- Logger, qui contient les différents façons d'afficher les résultats, une des façons est sur le terminal, l'autre sur discord.

## Résulats : 
### Avant optimisation : 
Temps d'exécution : 24.3995 secondes pour !inference pizza r_has_part mozza

### Avant optimisation et avec le cache: 
Temps d'exécution : 0.9891 secondes pour !inference pizza r_has_part mozza

### Après optimisation : 
Temps d'exécution : 1.8519 secondes pour !inference pizza r_has_part mozza

### Après optimisation et avec le cache: 
Temps d'exécution : 0.9288 secondes pour !inference pizza r_has_part mozza

## Ressource

- [test inférence](https://www.jeuxdemots.org/rezo-ask.php?question=pq+pizza+r_has_part+mozza%3F&text=1&gotermsubmit=Demander%2FR%E9pondre)
- [jdm api doc](https://jdm-api.demo.lirmm.fr/schema)
- [jdm relations](https://www.jeuxdemots.org/jdm-about-detail-relations.php)
- [instructions](https://docs.google.com/document/d/1njrZm9WEVkAM7zTXvnNMov-fR4KfbUn1DQ5V1AeRkR4/)
