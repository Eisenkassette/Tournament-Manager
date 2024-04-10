from views.view_main import ViewMain
from views.view_player import PlayerView
from views.view_tournament import TournamentView
from controllers.controller_player import PlayerController
from controllers.controller_tournament import TournamentController

main_view = ViewMain()
player_view = PlayerView()
player_controller = PlayerController()
tournament_view = TournamentView()
tournament_controller = TournamentController()


class MainController:

    @staticmethod
    def main_menu():
        while True:
            main_view.display_main_menu()
            choice = main_view.get_menu_choice()
            if choice == "1":
                MainController.player_section()
            elif choice == "2":
                MainController.tournament_section()
            elif choice == "3":
                print("Exiting...\n")
                break

    @staticmethod
    def tournament_section():
        while True:
            tournament_view.display_tournament_menu()
            choice = tournament_view.get_menu_choice()
            if choice == '1':
                basic_information = tournament_view.input_basic_tournament_info()
                if not basic_information:
                    print("Exiting...")
                    continue
                player_view.print_player_list(player_controller.list_players_from_db())
                participants_chessids = (tournament_view.input_players_to_add()).split("-")
                if not participants_chessids:
                    print("Exiting...")
                    continue
                print(participants_chessids)


            elif choice == '2':
                print("Tournament2")
            elif choice == '3':
                print("Tournament3")
            elif choice == '4':
                print("Tournament4")
            elif choice == '5':
                print("Exiting...\n")
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def player_section():
        while True:
            player_view.display_player_menu()
            choice = player_view.get_menu_choice()
            if choice == '1':
                player_info = player_view.input_player_info()
                if player_info is not None:
                    match = player_controller.find_player_by_chessid(player_info[3])
                    if not match:
                        player_controller.add_player(*player_info)
                        print("\nPlayer added successfully.")
                    else:
                        player_view.print_duplicate_players(player_controller.find_player_by_chessid(player_info[3]))
            elif choice == '2':
                player_view.print_player_list(player_controller.list_players_from_db())
            elif choice == '3':
                chess_id = player_view.ask_for_player_chessid()
                match = player_view.print_matching_players(player_controller.find_player_by_chessid(chess_id))
                if match is not None:
                    if player_view.confirm_delete_player() == "y":
                        player_controller.remove_player_by_chessid(chess_id)
                        print("Player(s) deleted")
                    else:
                        print("")
            elif choice == '4':
                print("Exiting...\n")
                break
            else:
                print("Invalid choice. Please try again.")
