# list of rounds here
from tinydb import TinyDB, Query
import os
from models.model_tournament import TournamentModel


class TournamentController:
    def __init__(self):
        db_path = 'data/tournaments.db.json'
        if not os.path.exists(db_path):
            open(db_path, 'w').close()

        self.db = TinyDB(db_path)
        self.table = self.db.table('tournaments')
        self.tournaments = self.list_tournaments_from_db()

    def list_tournaments_from_db(self):
        return [TournamentModel(**tournament) for tournament in self.table.all()]

    def find_tournament_by_name(self, tournament_name):
        return self.table.search(Query().tournament_name == str(tournament_name))

    def create_tournament(self,
                          tournament_name: str,
                          location: str,
                          max_round_number: int,
                          description: str,
                          participants: list):
        tournament = TournamentModel(tournament_name, location, max_round_number, description, "Not started",
                                     "Never Ended", 1, [], participants)
        self.table.insert(tournament.to_dict())
        self.tournaments.append(tournament)

    # def start_tournament(self, tournament_name: str):

    def remove_tournament_by_name(self, name: str):
        self.table.remove(Query().tournament_name == str(name))
        self.tournaments = [tournament for tournament in self.tournaments if tournament.tournament_name != str(name)]
