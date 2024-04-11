import re


class PlayerView:
    @staticmethod
    def display_player_menu():
        print("\nPlayer Management")
        print("1. Add a player")
        print("2. Display all players")
        print("3. Delete a player")
        print("4. Exit")

    @staticmethod
    def get_menu_choice():
        return input("Enter your choice: ")

    @staticmethod
    def input_player_info():
        print("\nAdd a Player")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")

        pattern = r'^(?!\d{2}-\d{2}-\d{4}$).*$'
        birthday = input("Enter date of birth (DD-MM-YYYY): ")
        while re.match(pattern, birthday):
            print("Please enter a valid birthday:")
            birthday = input("Enter date of birth (DD-MM-YYYY): ")

        chess_id = input("Enter chess ID: ")

        print("\nSummary: ", "\nFirst name: " + first_name, "\nLast name: " +
              last_name, "\nbirthday: " + birthday, "\nChess id: " + chess_id)

        while True:
            confirmation = input("Player information correct (y/n)? : ")
            if confirmation.lower() == "y":
                return first_name, last_name, birthday, chess_id
            elif confirmation.lower() == "n":
                print("Returning to main menu...")
                return None
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    @staticmethod
    def ask_for_player_chessid():
        chess_id = input("Enter chess ID of a player: ")
        return chess_id

    @staticmethod
    def print_duplicate_players(match):
        print("\nEntered chessid is already used.")
        print("Please delete the following player to use it:")
        print("--------------------")
        for player in match:
            print("Name:", player['first_name'], player['last_name'])
            print("Date of Birth:", player['birthday'])
            print("Chess ID:", player['chess_id'])
            print("--------------------")
        return "Not None"

    @staticmethod
    def print_matching_players(match):
        if not match:
            print("No players matched the chessid")
            return None
        else:
            print("Player with matched chessid: ")
            print("--------------------")
            for player in match:
                print("Name:", player['first_name'], player['last_name'])
                print("Date of Birth:", player['birthday'])
                print("Chess ID:", player['chess_id'])
                print("--------------------")
            return "Not None"

    @staticmethod
    def confirm_delete_player():
        while True:
            confirmation = input("Delete player? (y/n): ")
            if confirmation.lower() == "y" or confirmation.lower() == "n":
                return confirmation
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    @staticmethod
    def print_player_list(player_list):
        if not player_list:
            print("\nNo players")
        else:
            print("\nPlayers list: ")
            print("--------------------")
            for player in player_list:
                print("Name:", player.first_name, player.last_name)
                print("Date of Birth:", player.birthday)
                print("Chess ID:", player.chess_id)
                print("--------------------")
