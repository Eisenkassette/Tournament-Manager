class PlayerModel:
    def __init__(self, first_name, last_name, birthday, chess_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.chess_id = chess_id

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'chess_id': self.chess_id
        }
