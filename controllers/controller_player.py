from tinydb import TinyDB, Query
import os
from models.model_player import PlayerModel


class PlayerController:
    def __init__(self):
        db_path = 'data/players.db.json'
        if not os.path.exists(db_path):
            open(db_path, 'w').close()

        self.db = TinyDB(db_path)
        self.table = self.db.table('players')
        self.players = self.list_players_from_db()

    def list_players_from_db(self):
        return [PlayerModel(**player) for player in self.table.all()]

    def add_player(self, first_name, last_name, birthday, chess_id):
        player = PlayerModel(first_name, last_name, birthday, chess_id)
        self.table.insert(player.to_dict())
        self.players.append(player)

    def remove_player_by_chessid(self, chess_id):
        self.table.remove(Query().chess_id == str(chess_id))
        self.players = [player for player in self.players if player.chess_id != str(chess_id)]

    def find_player_by_chessid(self, chess_id):
        return self.table.search(Query().chess_id == str(chess_id))
