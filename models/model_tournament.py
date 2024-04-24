class TournamentModel:
    def __init__(self,
                 tournament_name: str,
                 location: str,
                 max_rounds_number: int,
                 description: str,
                 start_date,
                 end_date,
                 current_round_number,
                 rounds_list: list,
                 participants: list):
        self.tournament_name = tournament_name
        self.location = location
        self.max_rounds_number = max_rounds_number
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.current_round_number = current_round_number
        self.rounds_list = rounds_list
        self.participants = participants

    def to_dict(self):
        return {
            'tournament_name': self.tournament_name,
            'location': self.location,
            'max_rounds_number': self.max_rounds_number,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'current_round_number': self.current_round_number,
            'rounds_list': self.rounds_list,
            'participants': self.participants
        }
