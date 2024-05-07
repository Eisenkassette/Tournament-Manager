from tinydb import TinyDB
from datetime import datetime
import json
import os
from models.model_rounds import RoundsModel


class RoundsController:
    def __init__(self):
        self.matches = []
        self.participants = []
        self.db_folder = 'data/rounds/'
        if not os.path.exists(self.db_folder):
            os.makedirs(self.db_folder)

    def load_rounds_from_file(self, tournament_name):
        """
        load_rounds_from_file loads into memory all existing matches of a given tournament.

        Parameters:
        - tournament_name
        """
        db_file = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")
        if not os.path.exists(db_file):
            open(db_file, 'w').close()

        with open(db_file, 'r') as file:
            data = json.load(file)
            if "rounds" in data:
                rounds_data = data["rounds"]
                round_1_data = rounds_data.get("1", {})
                if round_1_data:
                    self.participants = round_1_data.get("participants", [])
                    self.matches = round_1_data.get("matches", [])

    def get_all_matches(self, tournament_name):
        """
        get_all_matches returns a list of all matches of a given tournament.

        Parameters:
        - tournament_name

        Returns:
        List of all rounds
        """
        db_file = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")
        all_rounds = []

        with open(db_file, 'r') as file:
            data = json.load(file)
            round_data = data["rounds"]
            for round_info in round_data.values():
                match_data = round_info.get("matches", [])
                all_rounds.extend(match_data)

        return all_rounds

    def load_latest_round_from_file(self, tournament_name):
        """
        load_latest_round_from_file loads the data from the file of a given tournament.

        Parameters:
        - tournament_name
        """
        db_file = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")

        with open(db_file, 'r') as file:
            data = json.load(file)
            if "rounds" in data:
                rounds_data = data["rounds"]
                latest_round_number = max(map(int, rounds_data.keys()), default=0)  # Get the latest round number
                latest_round_data = rounds_data.get(str(latest_round_number), {})  # Load data for the latest round
                if latest_round_data:
                    self.participants = latest_round_data.get("participants", [])
                    self.matches = latest_round_data.get("matches", [])

    def print_matches(self):
        """
        print_matches prints the currently loaded matches.

        Returns:
        matches
        """
        return self.matches

    def check_for_match_file(self, tournament_name: str):
        """
        check_for_match_file checks if a rounds' file corresponding to a specific tournament exists.

        Parameters:
        - tournament_name: str

        Returns:
        "Not Found" if file doesn't exist
        "File found" if file exists
        """
        db_path = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")
        if not os.path.exists(db_path):
            return "Not Found"
        else:
            return "File found"

    def delete_round_file(self, tournament_name):
        """
        delete_round_file deletes a round's file corresponding to a specific tournament.

        Parameters:
        - tournament_name: str
        """
        db_file = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")
        if os.path.exists(db_file):
            os.remove(db_file)

    def create_round_one(self, tournament_name: str, participants_list: list):
        """
        create_round_one generates the first round of the tournament.
        If the round's file doesn't exist it will create it.

        Parameters:
        - tournament_name: str
        - participants_list: list
        """
        db_path = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")
        if not os.path.exists(db_path):
            open(db_path, 'w').close()
        round_name = "Round 1"
        start_time = "None"
        for player in participants_list:
            player['score'] = 0
        sorted_players = sorted(participants_list, key=lambda x: x['score'])

        for i in range(0, len(sorted_players), 2):
            player_1_info = [sorted_players[i]['chess_id'], sorted_players[i]['score']]
            player_2_info = [sorted_players[i + 1]['chess_id'], sorted_players[i + 1]['score']] \
                if i + 1 < len(sorted_players) else None
            self.matches.append([player_1_info, player_2_info])

        round_1 = RoundsModel(start_time, round_name, participants_list, self.matches, start_time)

        db = TinyDB(db_path)
        table = db.table('rounds')
        table.insert(round_1.to_dict())

    def input_match_results(self):
        """
        input_match_results gets and updates player score for the loaded matches
        """
        for match in self.matches:
            player_1_info, player_2_info = match[0], match[1]
            player_1_name = self.get_player_name(player_1_info[0])
            player_2_name = self.get_player_name(player_2_info[0])

            print("--------------------------------")

            while True:
                winner_chess_id = input(f"{player_1_name} {player_1_info[0]} vs {player_2_name} {player_2_info[0]}"
                                        f"\nEnter winner chessid or type 'tie': ")

                if winner_chess_id.lower() == "tie":
                    self.update_score(player_1_info[0], 0.5)
                    self.update_score(player_2_info[0], 0.5)
                    match[0][1] = self.get_player_score(player_1_info[0])
                    match[1][1] = self.get_player_score(player_2_info[0])
                    break
                elif winner_chess_id == player_1_info[0]:
                    self.update_score(player_1_info[0], 1)
                    self.update_score(player_2_info[0], 0)
                    match[0][1] = self.get_player_score(player_1_info[0])
                    match[1][1] = self.get_player_score(player_2_info[0])
                    break
                elif winner_chess_id == player_2_info[0]:
                    self.update_score(player_1_info[0], 0)
                    self.update_score(player_2_info[0], 1)
                    match[0][1] = self.get_player_score(player_1_info[0])
                    match[1][1] = self.get_player_score(player_2_info[0])
                    break
                else:
                    print("Wrong input. Please input chessid of winner or 'tie'.")

    def create_next_round(self, tournament_name):
        """
        create_next_round generates a new round for a given tournament.

        Parameters:
        - tournament_name: str
        """
        db_file = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")
        next_round_number = self.get_highest_round_number(tournament_name) + 1

        # Load existing rounds data
        with open(db_file, 'r') as file:
            data = json.load(file)
            if "rounds" in data:
                rounds_data = data["rounds"]

                # Update participants list for the new round
                new_round_data = {
                    "round_name": f"Round {next_round_number}",
                    "start_time": "None",
                    "end_time": "None",
                    "participants": self.participants,
                    "matches": self.generate_matches_for_round(tournament_name)
                }

                # Append the new round data to the existing rounds data
                rounds_data[str(next_round_number)] = new_round_data

        # Write the updated rounds data back to the file
        with open(db_file, 'w') as file:
            json.dump(data, file, indent=4)

    def return_latest_matches(self, tournament_name):
        """
        return_latest_matches returns the list of current matches of a given tournament.

        Parameters:
        - tournament_name

        Returns:
        List of matches
        """
        matches = self.load_round_matches(tournament_name, self.get_highest_round_number(tournament_name))
        beautiful_matches = []
        for match in matches:
            player_1_id, player_1_score = match[0][0], match[0][1]
            player_2_id, player_2_score = match[1][0], match[1][1]

            # Format the match information
            formatted_match = f"{player_1_id} - score: {player_1_score} vs {player_2_id} - score: {player_2_score}"
            beautiful_matches.append(formatted_match)

        return '\n'.join(beautiful_matches)

    def load_round_matches(self, tournament_name, round_number):
        """
        load_round_matches returns the list of matches of a given round of a given tournament.

        Parameters:
        - tournament_name
        - round_number

        Returns:
        List of matches
        """
        db_file = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")

        with open(db_file, 'r') as file:
            data = json.load(file)
            if "rounds" in data:
                rounds_data = data["rounds"]
                round_data = rounds_data.get(str(round_number))
                if round_data:
                    return round_data.get("matches", [])
        return []

    def generate_matches_for_round(self, tournament_name):
        """
        generate_matches_for_round generates a list of matches for a given tournament.

        Parameters:
        - tournament_name: str

        Returns:
        List of matches
        """
        # Load the data from the latest round
        self.load_latest_round_from_file(tournament_name)

        # Sort participants based on their scores
        sorted_participants = sorted(self.participants, key=lambda participant: participant['score'], reverse=True)

        # Get the matches from the latest round
        latest_round_matches = self.matches

        latest_round_opponents = {}
        for match in latest_round_matches:
            for player_info in match:
                player_id = player_info[0]
                opponent_id = match[1 - match.index(player_info)][0]

                # Check if player_id is already in the dictionary
                if player_id not in latest_round_opponents:
                    # If not, add it with an empty set as the value
                    latest_round_opponents[player_id] = set()

                # Add opponent_id to the set of opponents for player_id
                latest_round_opponents[player_id].add(opponent_id)

        # Generate matches based on the sorted list of participants
        matches = []
        for i in range(0, len(sorted_participants), 2):
            player_1_id = sorted_participants[i]['chess_id']
            player_2_id = sorted_participants[i + 1]['chess_id']

            # Check if player 1 has played against player 2 in the latest round
            if player_2_id in latest_round_opponents.get(player_1_id, []):
                # If so, find a new opponent for player 2
                for j in range(i + 2, len(sorted_participants)):
                    player_2_id = sorted_participants[j]['chess_id']
                    if player_2_id not in latest_round_opponents.get(player_1_id, []):
                        break

            # Add the match to the list of matches
            matches.append([
                [player_1_id, sorted_participants[i]['score']],
                [player_2_id, sorted_participants[i + 1]['score']]
            ])

        return matches

    def get_player_score(self, chess_id):
        """
        get_player_score finds a player using his chess_id and returns his score.

        Parameters:
        - chess_id

        Returns:
        Player score
        """

        for participant in self.participants:
            if participant["chess_id"] == chess_id:
                return participant["score"]
        return 0

    def get_highest_round_number(self, tournament_name):
        """
        get_highest_round_number finds the highest round number of a given tournament.

        Parameters:
        - tournament_name

        Returns:
        Highest round number
        """
        db_file = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")

        with open(db_file, 'r') as file:
            data = json.load(file)
            if "rounds" in data:
                rounds_data = data["rounds"]
                if rounds_data:
                    highest_round_number = max(map(int, rounds_data.keys()))
                    return highest_round_number

    def get_player_name(self, chess_id):
        """
        get_player_name finds the name of a player matching the chess_id parameter.

        Parameters:
        - chess_id

        Returns:
        Player's first name, last name and chess_id
        """
        for participant in self.participants:
            if participant["chess_id"] == chess_id:
                return f"{participant['first_name']} {participant['last_name']} ({chess_id})"
        return "Unknown Player"

    def update_latest_match_data(self, tournament_name):
        """
        update_latest_match_data updates the score of the last existing round of a given tournament using
        the currently loaded data.

        Parameters:
        - tournament_name
        """
        db_file = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")

        with open(db_file, 'r+') as file:
            data = json.load(file)
            if "rounds" in data:
                rounds_data = data["rounds"]
                latest_round_number = max(map(int, rounds_data.keys()), default=0)
                latest_round_data = rounds_data.get(str(latest_round_number), {})

                if latest_round_data:
                    latest_round_data["participants"] = self.participants
                    latest_round_data["matches"] = self.matches

                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()

    def update_round_start_time(self, tournament_name, round_number):
        """
        update_round_start_time updates start_time of a given tournament's round with current data.

        Parameters:
        - tournament_name
        - round_number
        """
        db_file = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")
        start_time = datetime.now().strftime("%d-%m-%Y %H:%M")

        with open(db_file, 'r+') as file:
            data = json.load(file)
            if "rounds" in data:
                rounds_data = data["rounds"]
                if str(round_number) in rounds_data:
                    rounds_data[str(round_number)]["start_time"] = start_time
                    file.seek(0)  # Move the file pointer to the beginning
                    json.dump(data, file, indent=4)  # Write the updated data back to the file

    def update_round_end_time(self, tournament_name, round_number):
        """
        update_round_end_time updates end_time of a given tournament's round with current data.

        Parameters:
        - tournament_name
        - round_number
        """
        db_file = os.path.join(self.db_folder, f"{tournament_name}.rounds.db.json")
        end_time = datetime.now().strftime("%d-%m-%Y %H:%M")

        with open(db_file, 'r+') as file:
            data = json.load(file)
            if "rounds" in data:
                rounds_data = data["rounds"]
                if str(round_number) in rounds_data:
                    rounds_data[str(round_number)]["end_time"] = end_time
                    file.seek(0)  # Move the file pointer to the beginning
                    json.dump(data, file, indent=4)  # Write the updated data back to the file

    def update_score(self, chess_id, score):
        """
        update_score updates the score of a given player that is currently loaded.

        Parameters:
        - chess_id
        - score
        """
        for participant in self.participants:
            if participant["chess_id"] == chess_id:
                participant["score"] += score
                break
