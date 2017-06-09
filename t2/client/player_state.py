class PlayerState:
    player_data = {}
    instance = None

    def __init__(self):
        if self.instance is not None:
            raise ValueError("An instantiation already exists!")

    @classmethod
    def get_instance(cls):
       if cls.instance is None:
            cls.instance = PlayerState()
       return cls.instance

    def initialize(self, name):
        self.player_data['name'] = name
        return self.player_data

    def update_data(self, new_data):
        self.player_data = new_data
