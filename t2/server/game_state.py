class GameState:
    instance = None
    players = []

    def __init__(self):
        if self.instance is not None:
            raise ValueError("An instantiation already exists!")

    @classmethod
    def get_instance(cls):
       if cls.instance is None:
            cls.instance = GameState()
       return cls.instance

    def get_players(self):
        return self.players

    def get_player(self, player_name):
        if len(self.players) > 0:
            return next((player for player in self.players if player["name"] == player_name), None)
        return None
