import socket

class SocketHandler:
    instance = None
    s = None

    def __init__(self):
        if self.instance is not None:
            raise ValueError("An instantiation already exists!")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    @classmethod
    def get_instance(cls):
       if cls.instance is None:
            cls.instance = SocketHandler()
       return cls.instance

    def connect(self, host, port):
        if (host == ''):
            host = socket.gethostname()

        self.s.bind((host, port))
        print("Bind to: " + str(self.s.getsockname()))

    def send(self, message):
        self.s.send(message)

    def sendto(self, message, destination):
        print("Sent to: " + str(destination))
        self.s.sendto(message, destination)

    def receivefrom(self):
        return self.s.recvfrom(1024)

    def receive(self):
        return self.s.recv(1024)

    def close(self):
        self.s.close()
