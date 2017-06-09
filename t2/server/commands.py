import game_state
import common.socket_handler
import common.protocol

SocketHandler = common.socket_handler.SocketHandler.get_instance()
GameState = game_state.GameState.get_instance()

def create_player(received_address, data):
    data['pos_x'] = 1
    data['pos_y'] = 1
    GameState.get_players().append(data)
    message = common.protocol.encode(common.protocol.RESPONSE_EVENT['OK'], None)
    SocketHandler.sendto(message, received_address)
