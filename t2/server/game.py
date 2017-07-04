import common.socket_handler
import common.protocol
import commands
import log_handler
import game_state

GameState = game_state.GameState.get_instance()
SocketHandler = common.socket_handler.SocketHandler.get_instance(5001, 5002)

commands_handler = {
    common.protocol.GAME_EVENT['CREATE_PLAYER']: commands.create_player,
    common.protocol.GAME_EVENT['MOVE_PLAYER']: commands.move_player,
    common.protocol.GAME_EVENT['LIST_OBJECTS']: commands.list_objects
}

def initialize():
    log_handler.clear()

    port = 5002

    SocketHandler.connect('', port)

    print("Welcome to the server!")

def main_loop():
    while True:
        GameState.print_map_state()
        message, received_address = SocketHandler.receivefrom()

        log_handler.log(message)
        if not message:
            break

        command, data = common.protocol.decode(message)
        commands_handler[command](received_address, data)
    SocketHandler.close()

def run():
    initialize()

    main_loop()
