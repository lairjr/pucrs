import common.socket_handler
import common.protocol

SocketHandler = common.socket_handler.SocketHandler.get_instance()

player_data = {
    "name": ''
}

def initialize():
    global player_data

    player_data['name'] = raw_input("Give me your player name: ")

    message = common.protocol.encode(common.protocol.GAME_EVENT['CREATE_PLAYER'], player_data)
    SocketHandler.sendto(message, ("172.18.0.2", 5002))
