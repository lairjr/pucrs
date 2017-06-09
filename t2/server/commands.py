import game_state
import common.socket_handler
import common.protocol

SocketHandler = common.socket_handler.SocketHandler.get_instance()
GameState = game_state.GameState.get_instance()

def create_player(received_address, player_data):
    message = None

    if GameState.get_player(player_data['name']) is None:
        player_data['pos_x'] = 1
        player_data['pos_y'] = 1
        GameState.get_players().append(player_data)
        message = common.protocol.encode(common.protocol.RESPONSE_EVENT['OK'], None)
    else:
        message = common.protocol.encode(common.protocol.RESPONSE_EVENT['ERROR'], None)

    SocketHandler.sendto(message, received_address)
