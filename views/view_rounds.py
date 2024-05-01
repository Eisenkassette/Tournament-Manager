class RoundsView:

    @staticmethod
    def display_matches_and_round_name(current_round, current_matches):
        print("\nMatches list for Round", current_round, ": ")
        for match in current_matches:
            print("--------------------")
            print("ChessID:", match[0][0], "Score:", match[0][1], "VS", "ChessID:", match[1][0], "Score:", match[1][1])
