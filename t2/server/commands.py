import game_state
import common.socket_handler
import common.protocol

SocketHandler = common.socket_handler.SocketHandler.get_instance()
GameState = game_state.GameState.get_instance()

def create_player(received_address, player_data):
    message = None

    if GameState.get_player(player_data['name']) is None:
        player_data = GameState.add_player(player_data)
        message = common.protocol.encode(common.protocol.RESPONSE_EVENT['OK'], player_data)
    else:
        message = common.protocol.encode(common.protocol.RESPONSE_EVENT['ERROR'], None)

    SocketHandler.sendto(message, received_address)

def move_player(received_address, player_data):
    message = None

    player_data = GameState.update_players_state(player_data)
    message = common.protocol.encode(common.protocol.RESPONSE_EVENT['OK'], player_data)

    SocketHandler.sendto(message, received_address)

def list_objects(received_address, player_data):
    message = None

    objects = GameState.get_objects()
    message = common.protocol.encode(common.protocol.RESPONSE_EVENT['OK'], { "objects": objects })

    SocketHandler.sendto(message, received_address)
