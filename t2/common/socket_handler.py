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
        self.s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

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

        # eth_heeader =  struct.pack('!HHHH', self.source_port, self.destination_port, length, checksum)

        ip_ihl_ver = 5
        ip_tos = 4
        ip_tot_len = 0
        ip_id = 0
        ip_frag_off = 0
        ip_ttl = 255
        ip_proto = socket.IPPROTO_UDP
        ip_check = 0
        ip_saddr = self.s.getsockname()[0]
        ip_daddr = destination[0]
        ip_header = struct.pack('!BBHHHBBH4s4s' , ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)

        length = 8+len(message);
        checksum = 0
        udp_header = struct.pack('!HHHH', self.source_port, self.destination_port, length, checksum)

        self.s.sendto(ip_header + udp_header + message, destination)

    def receivefrom(self):
        packet, received_address = self.s.recvfrom(1024)
        return (str(packet)[28:], received_address)

    def close(self):
        self.s.close()
