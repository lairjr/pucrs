import game
import common.socket_handler

def Main():
    host = "server"
    port = 5002

    common.socket_handler.initialize(host, port)

    game.run(host, port)

if __name__ == '__main__':
    Main()
