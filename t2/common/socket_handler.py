import socket
import struct

class SocketHandler:
    instance = None
    s = None

    def __init__(self, destination_port, source_port):
        if self.instance is not None:
            raise ValueError("An instantiation already exists!")
        self.destination_port = destination_port
        self.source_port = source_port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

    @classmethod
    def get_instance(cls, destination_port, source_port):
       if cls.instance is None:
            cls.instance = SocketHandler(destination_port, source_port)
       return cls.instance

    def connect(self, host, port):
        if (host == ''):
            host = socket.gethostname()

        self.s.bind((host, port))
        print("Bind to: " + str(self.s.getsockname()))

    def sendto(self, message, destination):
        print("Sent to: " + str(destination))

        length = 8+len(message);
        checksum = 0
        udp_header = struct.pack('!HHHH', self.source_port, self.destination_port, length, checksum)
        self.s.sendto(udp_header + message, destination)

    def receivefrom(self):
        packet, received_address = self.s.recvfrom(1024)
        return (str(packet)[28:], received_address)

    def close(self):
        self.s.close()
