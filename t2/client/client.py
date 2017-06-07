import game
import socket_handler

def Main():
    host = "server"
    port = 5002

    socket_handler.initialize(host, port)

    game.run(host, port)

if __name__ == '__main__':
    Main()
