<h2> Gestionnaire de tournoi d'Echecs </h2>

TournamentManager est un logiciel en ligne de commande pour gérer des tournois d'échecs.

<h3> Utilisation </h3>
Télécharger le dossier.<br>
Utilisez un terminal pour vous positionner dans le dossier principal, celui-ci contient un fichier nommé requirements.txt et main.py.<br>

Taper: ```pip install -r requirements.txt``` pour installer les libraries requises.

Taper: ```python3 main.py``` pour lancer le logiciel.

<h3> Stockage d'information </h3>

Le logiciel va crée un dossier data à la racine de main.py.<br>
Le dossier data va contenir :

- "player.db.json", contenant les informations des joueurs<br>
- "tournaments.db.json", contenant les informations des tournois<br>
- Un dossier "rounds", contenant des fichiers json unique à chaques tournois.

Les données sont mises à jour au fil des opérations et son chargé durant le démarrage.

<h3> Verification Flake8 </h3>

Pour vérifier la conformité du code au règles PEP8, ouvre un terminal, positionner vous dans le dossier contenant main.py.<br>
Puis entrer les commandes suivantes :

- ```pip install flake8```
- ```flake8  --max-line-length 119 --format=html --htmldir=flake8_rapport```

Le fichier "flake8_rapport" sera mis à jour.