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
