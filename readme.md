<h2> Gestionnaire de tournoi d'Echecs </h2>
TournamentManager est un logiciel en ligne de commande pour gerer des tounois d'echecs.
<h3> Utilisation </h3>
Telecharger le dossier.<br>
Utilisez un terminal pour vous positionner dans le dossier principal, celui-ci contient un fichier nommer requirements.txt et main.py.<br>

Taper: ```pip install -r requirements.txt``` pour installer les libraries requises.

Taper: ```python3 main.py``` pour lancer le logiciel.

<h3> Stockage d'information </h3>

Le logiciel va cree un un dossier data a la racine de main.py.<br>
Le dossier data va contenir:

- "player.db.json", contenant les informations des joueurs<br>
- "tournaments.db.json", contenant les informations des tournois<br>
- un dossier "rounds", contenant des fichiers json unique a chaque tournoi stockant tous les matches.
