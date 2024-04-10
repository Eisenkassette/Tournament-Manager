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
              location, "\nNumber of rounds: " + max_round_number, "\nDescription: " + description)
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
    def input_players_to_add():
        print("Enter chess IDs of participants (chessid1-chessid2-etc...)")
        chess_id_list = input("List:")
        while True:
            print(chess_id_list)
            confirmation = input("List of participants correct (y/n)? : ")
            if confirmation.lower() == "y":
                return chess_id_list
            elif confirmation.lower() == "n":
                print("Returning to main menu...")
                return None
            else:
                print("Invalid input. Please enter 'y' or 'n'.")