from views.view_player import ViewPlayer


class ViewMain:

    @staticmethod
    def display_main_menu():
        print("1. Add a player")
        print("2. Display all players")
        print("3. Delete a player")
        print("4. exit")

    @staticmethod
    def user_input_main_menu():
        choice = input("Select option: ")
        if choice == "1":
            ViewPlayer.create_new_player()
        elif choice == "2":
            ViewPlayer.display_all_players()
        elif choice == "3":
            ViewPlayer.delete_a_player()
        elif choice == "4":
            raise SystemExit()
