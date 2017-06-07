import socket

def send():
    s.send("a")
    data = s.recv(1024)
    print("received from server: " + str(data))

def tips():
    print("available commands:")
    print("exit - will exit the game;")
    print("tips - will print available commands;")

commands = {
    "tips" : tips,
    "send" : send
}

def Main():
    host = "server"
    port = 5002

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host,port))

    message = raw_input("command: ")

    while message != "exit":
        commands[message]();
        message = raw_input("command: ")

    s.close()

if __name__ == '__main__':
    Main()
