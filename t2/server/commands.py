import common.socket_handler

handler = common.socket_handler.SocketHandler.get_instance()

def create_player(data):
    print("create player" + str(data))
