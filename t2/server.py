import socket
import sys

def Main():
    out_string = ""
    # set up host on my own computer
    host = socket.gethostname()
    port = 5002
    #create socket obj
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bind socket to port @ host, port
    s.bind((host, port))
    while True:
        print >>sys.stderr, '\nwaiting to receive message'
        data, receive_address = s.recvfrom(1024)
        out_file = open("Client_Data.txt", "w")
        out_string += str(data)
        out_string += "\n"
        out_file.write(out_string)
        if not data:
            break

        print(str(data))
        s.sendto(" Wubalabadubdub!!!!", receive_address)
    s.close()

if __name__ == '__main__':
        Main()
