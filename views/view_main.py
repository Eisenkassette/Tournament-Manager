class ViewMain:

    @staticmethod
    def display_main_menu():
        print("1. Player Management")
        print("2. Tournament Management")
        print("3. Reports")
        print("4. exit")

    @staticmethod
    def get_menu_choice():
        return input("Enter your choice: ")
