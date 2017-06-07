import common.socket_handler

def send():
    common.socket_handler.send("a")
    data = common.socket_handler.receive()
    print("received from server: " + str(data))

def tips():
    print("available commands:")
    print("exit - will exit the game;")
    print("tips - will print available commands;")
