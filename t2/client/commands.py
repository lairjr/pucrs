import common.socket_handler

handler = common.socket_handler.SocketHandler.get_instance()

def send():
    handler.sendto("a", ("172.18.0.2", 5002))
    data = handler.receivefrom()
    print("received from server: " + str(data))

def tips():
    print("available commands:")
    print("exit - will exit the game;")
    print("tips - will print available commands;")
