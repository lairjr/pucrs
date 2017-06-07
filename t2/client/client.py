import socket
import commands

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

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host,port))

    main_loop()

    s.close()

if __name__ == '__main__':
    Main()
