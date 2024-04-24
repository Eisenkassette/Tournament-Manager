from views.view_main import ViewMain
from views.view_player import PlayerView
from views.view_tournament import TournamentView
from views.view_rounds import RoundsView
from views.view_reports import ViewReports
from controllers.controller_player import PlayerController
from controllers.controller_tournament import TournamentController
from controllers.controller_rounds import RoundsController

main_view = ViewMain()
player_view = PlayerView()
rounds_view = RoundsView()
reports_view = ViewReports()
player_controller = PlayerController()
tournament_view = TournamentView()
tournament_controller = TournamentController()
rounds_controller = RoundsController()


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
                MainController.reports_section()
            elif choice == "4":
                print("Exiting...\n")
                break

    @staticmethod
    def reports_section():
        while True:
            reports_view.display_main_menu()
            choice = reports_view.get_menu_choice()
            if choice == "1":
                reports_view.print_player_list(player_controller.list_players_from_db())
            if choice == "2":
                tournament_view.print_tournament_list(tournament_controller.list_tournaments_from_db())
            if choice == "3":
                while True:
                    tournament_name = reports_view.ask_tournament_name()
                    tournament_date = tournament_controller.get_date_using_name(tournament_name)
                    if tournament_date:
                        reports_view.print_tournament_results(tournament_name, tournament_date)
                        break
                    else:
                        print("No tournament matched the name")
            if choice == "4":
                reports_view.print_participants_list(tournament_controller.find_participants_list_using_name(
                    reports_view.ask_tournament_name()))
            if choice == "5":
                tournament_name = reports_view.ask_tournament_name()
                reports_view.display_matches_and_rounds(rounds_controller.get_all_matches(tournament_name),
                                                        tournament_controller.find_participants_list_using_name(
                                                            tournament_name))
            elif choice == "6":
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
                match = tournament_controller.find_tournament_by_name(basic_information[1])
                if match:
                    print("The tournament with this name already exists:")
                    print(basic_information[1])
                    continue
                player_view.print_player_list(player_controller.list_players_from_db())
                participants_chessids = tournament_view.input_players_to_add()
                if not participants_chessids:
                    print("Exiting...")
                    continue
                participant_list = player_controller.create_player_list(participants_chessids)
                tournament_controller.create_tournament(*basic_information, participant_list)
                print("Tournament Created")
            elif choice == '2':
                tournament_view.print_tournament_list(tournament_controller.list_tournaments_from_db())
            elif choice == '3':
                tournament_view.print_tournament_list(tournament_controller.list_tournaments_from_db())
                tournament_name = tournament_view.ask_for_tournament_name()
                match = tournament_controller.find_tournament_by_name(tournament_name)
                if match:
                    tournament_controller.set_tournament_start_date(tournament_name)
                    tournament_controller.launch_tournament(tournament_name)
                else:
                    print("No matching tournament found")
            elif choice == '4':
                tournament_view.print_tournament_list(tournament_controller.list_tournaments_from_db())
                tournament_name = tournament_view.ask_for_tournament_name()
                match = tournament_controller.find_tournament_by_name(tournament_name)
                if match:
                    tournament_view.print_matching_names(match)
                    if tournament_view.confirm_delete_tournament() == "y":
                        tournament_controller.remove_tournament_by_name(tournament_name)
                        print("\nTournament Deleted")
                    else:
                        print("Exiting...\n")
                        continue
                else:
                    print("\nNo Tournament matched that name.")
                    print("Exiting...\n")
                    continue
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
                player_view.print_player_list(player_controller.list_players_from_db())
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
