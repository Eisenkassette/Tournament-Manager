class TournamentView:
    @staticmethod
    def display_tournament_menu():
        print("\nTournament Management")
        print("1. Create Tournament")
        print("2. Display existing tournaments")
        print("3. Launch/resume tournament")
        print("4. Delete a tournament")
        print("5. Exit")

    @staticmethod
    def get_menu_choice():
        return input("Enter your choice: ")

    @staticmethod
    def input_basic_tournament_info():
        print("\nCreate a Player")
        tournament_name = input("Enter tournament name: ")
        location = input("Enter location: ")
        max_round_number = input("Enter number of rounds(or leave blank for 4): ")
        if not max_round_number:
            max_round_number = 4
        description = input("Enter description: ")
        print("\nSummary: ", "\nTournament name: " + tournament_name, "\nLocation: " +
              location, "\nNumber of rounds: ", max_round_number, "\nDescription: " + description)
        while True:
            confirmation = input("Tournament information correct (y/n)? : ")
            if confirmation.lower() == "y":
                return tournament_name, location, max_round_number, description
            elif confirmation.lower() == "n":
                print("Returning to main menu...")
                return None
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    @staticmethod
    def print_tournament_list(tournament_list):
        if not tournament_list:
            print("\nNo tournaments found")
            return None
        else:
            print("\nList of tournaments: ")
            print("--------------------")
            for tournament in tournament_list:
                print("Tournament name:", tournament.tournament_name)
                print("location:", tournament.location)
                print("Description:", tournament.description)
                print("--------------------")
            return "Not None"

    @staticmethod
    def ask_for_tournament_name():
        tournament_name = input("Enter name of Tournament: ")
        return tournament_name

    @staticmethod
    def print_matching_names(match):
        if not match:
            print("\nNo Tournament matched the name")
            return None
        else:
            print("\nTournament name matched: ")
            print("--------------------")
            for tournament in match:
                print("Tournament name:", tournament['tournament_name'])
                print("location:", tournament['location'])
                print("Description:", tournament['description'])
                print("--------------------")
            return "Not None"

    @staticmethod
    def confirm_delete_tournament():
        while True:
            confirmation = input("Delete Tournament? (y/n): ")
            if confirmation.lower() == "y" or confirmation.lower() == "n":
                return confirmation
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    @staticmethod
    def input_players_to_add():
        print("Enter chess IDs of participants (chessid1-chessid2-etc...)")
        chess_id_list = input("List:")
        while True:
            print(chess_id_list)
            confirmation = input("List of participants correct (y/n)? : ")
            if confirmation.lower() == "y":
                return chess_id_list.split("-")
            elif confirmation.lower() == "n":
                print("Returning to main menu...")
                return None
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
