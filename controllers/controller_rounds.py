from tinydb import TinyDB, Query
from datetime import datetime
import random
import os
from models.model_rounds import RoundsModel


class RoundsController:
    def __init__(self):
        self.matches = []
        self.db_folder = 'data/rounds/'
        if not os.path.exists(self.db_folder):
            os.makedirs(self.db_folder)

    def load_rounds_from_file(self, tournament_name):
        db_file = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")
        if not os.path.exists(db_file):
            open(db_file, 'w').close()

        db = TinyDB(db_file)
        table = db.table('rounds')
        return [RoundsModel(**rounds) for rounds in table.all()]

    def print_matches(self):
        return self.matches

    def create_round_zero(self, tournament_name: str, participants_list: list):
        db_path = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")
        if not os.path.exists(db_path):
            open(db_path, 'w').close()
        round_name = "Round 0"
        start_time = datetime.now().strftime("%d-%m-%Y %H:%M")
        for player in participants_list:
            player['score'] = 0
        sorted_players = sorted(participants_list, key=lambda x: x['score'])

        for i in range(0, len(sorted_players), 2):
            player_1_info = [sorted_players[i]['chess_id'], sorted_players[i]['score']]
            player_2_info = [sorted_players[i + 1]['chess_id'], sorted_players[i + 1]['score']] \
                if i + 1 < len(sorted_players) else None
            self.matches.append([player_1_info, player_2_info])

        round_0 = RoundsModel(start_time, round_name, participants_list, self.matches, start_time)

        print(self.matches)
        db = TinyDB(db_path)
        table = db.table('rounds')
        table.insert(round_0.to_dict())
