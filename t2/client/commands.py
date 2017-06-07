def send():
    s.send("a")
    data = s.recv(1024)
    print("received from server: " + str(data))

def tips():
    print("available commands:")
    print("exit - will exit the game;")
    print("tips - will print available commands;")
