from tinydb import TinyDB, Query
import os
from datetime import datetime
from controllers.controller_rounds import RoundsController
from models.model_tournament import TournamentModel

controller_rounds = RoundsController()


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

    def find_participants_list_using_name(self, tournament_name):
        result = self.table.search(Query().tournament_name == str(tournament_name))
        if result:
            return result[0]["participants"]
        else:
            return None

    def get_date_using_name(self, tournament_name):
        result = self.table.search(Query().tournament_name == str(tournament_name))
        if result:
            return result[0]["start_date"]
        else:
            return None

    def create_tournament(self,
                          tournament_name: str,
                          location: str,
                          max_rounds_number: int,
                          description: str,
                          participants: list):
        tournament = TournamentModel(tournament_name, location, max_rounds_number, description, -1,
                                     -1, 1, [], participants)
        self.table.insert(tournament.to_dict())
        self.tournaments.append(tournament)

    def set_tournament_start_date(self, tournament_name: str):
        current_tournament = self.table.get(Query().tournament_name == str(tournament_name))
        if current_tournament:
            if current_tournament.get('start_date', -1) == -1:
                current_time = datetime.now().strftime("%d-%m-%Y %H:%M")
                self.table.update({'start_date': current_time}, Query().tournament_name == tournament_name)
                for tournament in self.tournaments:
                    if tournament.tournament_name == tournament_name:
                        tournament.start_date = current_time
                        break

    def get_players_info(self, tournament_name: str):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            participants = tournament[0]['participants']
            players_info = []
            for player_data in participants:
                for player in player_data:
                    players_info.append(player)
            return players_info
        else:
            print("Tournament not found.")
            return None

    def get_max_rounds_number(self, tournament_name: str):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            return tournament[0]['max_rounds_number']
        else:
            print("Tournament not found.")
            return None

    def launch_tournament(self, tournament_name: str):
        participants_list = self.get_players_info(tournament_name)
        max_round_number = int(self.get_max_rounds_number(tournament_name))
        check = controller_rounds.check_for_match_file(tournament_name)
        if check == "Not Found":
            controller_rounds.create_round_one(tournament_name, participants_list)
        while True:
            controller_rounds.load_latest_round_from_file(tournament_name)
            controller_rounds.update_round_start_time(tournament_name,
                                                      controller_rounds.get_highest_round_number(tournament_name))
            controller_rounds.input_match_results()
            controller_rounds.update_round_end_time(tournament_name,
                                                    controller_rounds.get_highest_round_number(tournament_name))
            controller_rounds.update_latest_match_data(tournament_name)
            if int(controller_rounds.get_highest_round_number(tournament_name)) == max_round_number:
                break
            if int(controller_rounds.get_highest_round_number(tournament_name)) < max_round_number:
                controller_rounds.create_next_round(tournament_name)

    def remove_tournament_by_name(self, name: str):
        self.table.remove(Query().tournament_name == str(name))
        self.tournaments = [tournament for tournament in self.tournaments if tournament.tournament_name != str(name)]
        controller_rounds.delete_round_file(name)
