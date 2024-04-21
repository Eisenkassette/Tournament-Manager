class RoundsModel:
    def __init__(self, start_time, round_name, participants, matches=None, end_time=-1):
        self.round_name = round_name
        self.start_time = start_time
        self.end_time = end_time
        self.participants = participants
        self.matches = matches if matches is not None else []

    def to_dict(self):
        return {
            'round_name': self.round_name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'participants': self.participants,
            'matches': self.matches
        }
