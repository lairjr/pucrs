from functools import partial

class GameState:
    instance = None
    players = []
    objects = [
        { "name": "mapa", "can_pick": "true" },
        { "name": "porta", "can_pick": "false" }
    ]

    # MAP 30 x 10
    map = [
        [ "+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+" ],
        [ "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|" ],
        [ "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|" ],
        [ "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|" ],
        [ "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|" ],
        [ "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|" ],
        [ "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|" ],
        [ "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|" ],
        [ "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|" ],
        [ "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|" ],
        [ "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|" ],
        [ "+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+" ]
    ]

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

    def add_player(self, player_data):
        (pos_x, pos_y) = self.get_middle_map()
        player_data['pos_x'] = pos_x
        player_data['pos_y'] = pos_y
        self.players.append(player_data)
        self.update_map()

        return player_data

    def update_players_state(self, player_data):
        for index, player in enumerate(self.players):
            if player['name'] == player_data['name']:
                self.map[player['pos_y']][player['pos_x']] = ' '
                self.players[index] = player_data

        self.update_map()
        return player_data

    def print_map_state(self):
        print("\n".join(["".join([item for item in row]) for row in self.map]))

    def get_middle_map(self):
        return (15, 5)

    def update_map(self):
        for player in self.players:
            self.map[player['pos_y']][player['pos_x']] = 'o'

    def get_objects(self):
        return self.objects
