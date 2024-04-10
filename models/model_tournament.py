import datetime


class TournamentModel:
    def __init__(self, tournament_name: str, location: str, max_round_number: int, participants_chessid: list,
                 description: str):
        self.tournament_name = tournament_name
        self.location = location
        self.start_date = "Not Started"
        self.end_date = "Never Ended"
        self.max_round_number = max_round_number
        self.current_round_number = 0
        self.rounds_list = []
        self.participants_chessid = participants_chessid
        self.description = description

    def to_dict(self):
        return {
            'tournament_name': self.tournament_name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'round_number': self.max_round_number,
            'current_round_number': self.current_round_number,
            'rounds_list': self.rounds_list,
            'participants_chessid': self.participants_chessid,
            'description': self.description
        }
