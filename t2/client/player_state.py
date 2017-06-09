import common.socket_handler
import common.protocol

class PlayerState:
    SocketHandler = common.socket_handler.SocketHandler.get_instance()
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

    def initialize(self):
        self.player_data['name'] = raw_input("Give me your player name: ")

        message = common.protocol.encode(common.protocol.GAME_EVENT['CREATE_PLAYER'], self.player_data)
        self.SocketHandler.sendto(message, ("172.18.0.2", 5002))

        response, received_address = self.SocketHandler.receivefrom()
        (response_event, data) = common.protocol.decode(response)
        if response_event is not common.protocol.RESPONSE_EVENT['OK']:
            print("Erro ao criar jogador, tente novamente")
            self.initialize()
