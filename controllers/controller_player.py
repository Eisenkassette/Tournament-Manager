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
        """
        Returns:
        A list of all players in the database
        """
        return [PlayerModel(**player) for player in self.table.all()]

    def add_player(self, first_name, last_name, birthday, chess_id):
        """
        add_player creates a player in the database using the provided data

        Parameters:
        - first_name: Player's first name
        - last_name: Player's last name
        - birthday: Player's birthday
        - chess_id: Player's unique chess id
        """
        player = PlayerModel(first_name, last_name, birthday, chess_id)
        self.table.insert(player.to_dict())
        self.players.append(player)

    def remove_player_by_chessid(self, chess_id):
        """
        remove_player_by_chessid removes a player from the database using the unique chess_id parameter

        Parameters:
        - chess_id: Player's unique chess id
        """
        self.table.remove(Query().chess_id == str(chess_id))
        self.players = [player for player in self.players if player.chess_id != str(chess_id)]

    def find_player_by_chessid(self, chess_id):
        """
        find_player_by_chessid finds a player from the database using the unique chess_id parameter

        Parameters:
        - chess_id: Player's unique chess id

        Returns:
        Matching player list of information
        """
        return self.table.search(Query().chess_id == str(chess_id))

    def create_player_list(self, chess_id_list):
        """
        create_player_list finds all player matching the chess_id_list parameter and creates a list with all the data
        of each player.

        Parameters:
        - chess_id_list: list of chess_ids

        Returns:
        All matching players' data in a list
        """
        list_of_players = []
        for participant in chess_id_list:
            list_of_players.append(PlayerController.find_player_by_chessid(self, participant))
        return list_of_players
