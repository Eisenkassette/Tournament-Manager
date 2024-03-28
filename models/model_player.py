from tinydb import TinyDB, Query
import os


class ModelPlayer:
    # To rename the .json file or to change the path, simply edit the string below:
    player_database_path = "data/player_database.json"
    player_database = TinyDB(player_database_path)
    players_list = []

    def __init__(self, first_name, last_name, birthday, chess_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.chess_id = chess_id

    @classmethod
    def create_player(cls, first_name, last_name, birthday, chess_id):
        new_player = cls(first_name, last_name, birthday, chess_id)
        cls.players_list.append(new_player)
        cls.player_database.insert({'first_name': new_player.first_name, 'last_name': new_player.last_name,
                                    'birthday': new_player.birthday, 'chess_id': new_player.chess_id})
        return new_player

    @classmethod
    def delete_player(cls, chess_id):
        # Find the player with the specified chess_id
        chess_id = str(chess_id)
        user = Query()
        player_to_delete = cls.player_database.get(user.chess_id == chess_id)

        if player_to_delete:
            # Remove the player from players_list
            cls.players_list = [player for player in cls.players_list if player.chess_id != chess_id]

            # Remove the player from the database
            cls.player_database.remove(user.chess_id == chess_id)
            print("Player deleted successfully.")
            ModelPlayer.write_players_to_db()
        else:
            print("Player not found.")

    @classmethod
    def write_players_to_db(cls):
        # Clear the database
        cls.player_database.truncate()
        # Write each player in the list to the database
        for player in cls.players_list:
            cls.player_database.insert({'first_name': player.first_name, 'last_name': player.last_name,
                                        'birthday': player.birthday, 'chess_id': player.chess_id})

    @classmethod
    def check_for_db(cls):
        # Check if player_database.json exists
        if os.path.exists(cls.player_database_path):
            return "already exists"
        else:
            # Create the player_database.json file if it doesn't exist
            with open(cls.player_database_path, 'w') as file:
                pass
            return "db file created"

    def get_player_name(self):
        return self.first_name + " " + self.last_name

    @classmethod
    def load_players_from_db(cls):
        players_data = cls.player_database.all()
        cls.players_list = []
        for player_data in players_data:
            player = cls(player_data['first_name'], player_data['last_name'], player_data['birthday'],
                         player_data['chess_id'])
            cls.players_list.append(player)
        return cls.players_list
