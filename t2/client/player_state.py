class PlayerState:
    player_data = {}
    instance = None
    server_ip = None

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

    def move(self, direction):
        if direction is 'w':
            self.player_data['pos_y'] += 1
        if direction is 'd':
            self.player_data['pos_x'] += 1
        if direction is 's':
            self.player_data['pos_y'] += -1
        if direction is 'a':
            self.player_data['pos_x'] += -1

        return self.player_data

    def set_server_ip(self, server_ip):
        self.server_ip = server_ip
