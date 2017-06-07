import socket_handler

name = ''

def initialize():
    global name
    name = raw_input("Give me your player name: ")
    socket_handler.send("create player: " + str(name))
