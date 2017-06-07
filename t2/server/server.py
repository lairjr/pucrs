import socket
import sys
import os

def log(data):
    out_file = open("log.txt", "a+")
    out_string = str(data)
    out_string += "\n"
    out_file.write(out_string)

def Main():
    os.remove("log.txt")
    out_string = ""
    # set up host on my own computer
    host = socket.gethostname()
    port = 5002
    #create socket obj
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bind socket to port @ host, port
    s.bind((host, port))
    while True:
        print >> sys.stderr, '\nwaiting to receive messages'
        data, received_address = s.recvfrom(1024)

        log(data)
        if not data:
            break

        print(str(data))
        s.sendto(" Wubalabadubdub!!!!", received_address)
    s.close()

if __name__ == '__main__':
        Main()
