import game_state

GameState = game_state.GameState.get_instance()

def create_player(data):
    data['pos_x'] = 1
    data['pos_y'] = 1
    GameState.get_players().append(data)
