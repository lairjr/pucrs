import common.socket_handler
import common.protocol
import commands
import log_handler


handler = common.socket_handler.SocketHandler.get_instance()

commands = {
    common.protocol.actions()['CREATE_PLAYER']: commands.create_player
}

def initialize():
    log_handler.clear()

    port = 5002

    handler.connect('', port)

    print("Welcome to the server!")

def main_loop():
    while True:
        print("Waiting to receive commands...")
        message, received_address = handler.receivefrom()

        log_handler.log(message)
        if not message:
            break

        command, data = common.protocol.decode(message)
        commands[command](data)
    handler.close()

def run():
    initialize()

    main_loop()
