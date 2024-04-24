class ViewReports:

    @staticmethod
    def display_main_menu():
        print("\n1. List all player in Alpha order")
        print("2. List all tournaments")
        print("3. Name and date of given tournament")
        print("4. All tournament participants in Alpha order")
        print("5. List of all rounds and matches of a tournament")
        print("6. Exit")

    @staticmethod
    def get_menu_choice():
        return input("Enter your choice: ")

    @staticmethod
    def display_matches_and_rounds(matches_list, participants_list):
        print("\nRounds & Matches list: ")
        matches_per_round = len(participants_list)/2
        i = 0
        r = 1
        for match in matches_list:
            if i % matches_per_round == 0:
                print("Round", r, ":")
                r += 1
            print("ChessID:", match[0][0], "Score:", match[0][1], "VS", "ChessID:", match[1][0], "Score:", match[1][1])
            i += 1

    @staticmethod
    def ask_tournament_name():
        return input("\nEnter tournament name: ")

    @staticmethod
    def print_tournament_results(tournament_name, tournament_date):
        print("--------------------")
        print("Name: ", tournament_name)
        print("Start date: ", tournament_date)
        print("--------------------")

    @staticmethod
    def print_player_list(player_list):
        if not player_list:
            print("\nNo players")
        else:
            # Sort the player list based on the first name
            sorted_players = sorted(player_list, key=lambda player: player.first_name)

            print("\nPlayers list: ")
            print("--------------------")
            for player in sorted_players:
                print("Name:", player.first_name, player.last_name)
                print("Date of Birth:", player.birthday)
                print("Chess ID:", player.chess_id)
                print("--------------------")

    @staticmethod
    def print_participants_list(participant_list):
        if not participant_list:
            print("\nNo players")
        else:
            all_participants = [participant for sublist in participant_list for participant in sublist]
            # Sort the player list based on the first name
            sorted_players = sorted(all_participants, key=lambda participant: participant["first_name"])

            print("\nParticipants list: ")
            print("--------------------")
            for participant in sorted_players:
                print("Name:", participant["first_name"], participant["last_name"])
                print("Date of Birth:", participant["birthday"])
                print("Chess ID:", participant["chess_id"])
                print("--------------------")
