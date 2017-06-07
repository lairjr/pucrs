import socket_handler

def send():
    socket_handler.send("a")
    data = socket_handler.receive()
    print("received from server: " + str(data))

def tips():
    print("available commands:")
    print("exit - will exit the game;")
    print("tips - will print available commands;")
