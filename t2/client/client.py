import commands
import socket_handler

commands = {
    "tips" : commands.tips,
    "send" : commands.send
}

def main_loop():
    message = raw_input("command: ")

    while message != "exit":
        commands[message]();
        message = raw_input("command: ")

def Main():
    host = "server"
    port = 5002

    socket_handler.initialize(host, port)

    main_loop()

    socket_handler.close()

if __name__ == '__main__':
    Main()
