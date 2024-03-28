from models.model_player import ModelPlayer
from views.view_main import ViewMain


def main():
    ModelPlayer.check_for_db()
    ModelPlayer.load_players_from_db()

    while True:
        ViewMain.display_main_menu()
        ViewMain.user_input_main_menu()


if __name__ == "__main__":
    main()
