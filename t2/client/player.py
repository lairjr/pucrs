import socket_handler
import protocol

player_data = {
    "name": ''
}

def initialize():
    global player_data
    player_data['name'] = raw_input("Give me your player name: ")
    message = protocol.encode(protocol.actions()['CREATE_PLAYER'], player_data)
    socket_handler.send(message)
