class Player:
    def __init__(self, first_name, last_name, birthday, chess_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.chess_id = chess_id

    @classmethod
    def create(cls, first_name, last_name, birthday, chess_id):
        return cls(first_name, last_name, birthday, chess_id)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.birthday} ({self.chess_id})"


player_1 = Player("John", "Smith", "12042024", "D998293")
print(player_1.__str__())