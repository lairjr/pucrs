import socket

def Main():
    host = "server"
    port = 5002
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host,port))
    message = raw_input("please put message ")
    while message != "q":
        s.send(message)
        data = s.recv(1024)
        print("received from server: " + str(data))
        message = raw_input("please put message ")
    s.close()

if __name__ == '__main__':
    Main()
