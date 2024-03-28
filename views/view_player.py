from models.model_player import ModelPlayer


class ViewPlayer:

    @staticmethod
    def create_new_player():
        first_name = input("first name:")
        last_name = input("last name:")
        birth_date = input("birth date:")
        chess_id = input("chess id:")
        print("first name: ", first_name, " last name: ", last_name, " birth date: ", birth_date,
              " chess_id: ", chess_id)
        while True:
            user_confirmation = input("Confirm and create player? (y/n)")
            if user_confirmation.lower() == 'y':
                ModelPlayer.create_player(first_name, last_name, birth_date, chess_id)
                break
            elif user_confirmation.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n': ")

    @staticmethod
    def display_all_players():
        print(" ")
        print("FName LName Birthday ChessID")
        for player in ModelPlayer.players_list:
            print(player.first_name, player.last_name, player.birthday, player.chess_id)
        print(" ")

    @staticmethod
    def delete_a_player():
        chess_id_to_delete = input("Enter Chess id of player to delete: ")
        ModelPlayer.delete_player(chess_id_to_delete)

