import socket
import sys
import log_handler

def Main():
    log_handler.clear()

    host = socket.gethostname()
    port = 5002
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    while True:
        print >> sys.stderr, '\nwaiting to receive messages'
        message, received_address = s.recvfrom(1024)

        log_handler.log(message)
        if not message:
            break

        print(str(message))
        s.sendto(" Wubalabadubdub!!!!", received_address)
    s.close()

if __name__ == '__main__':
        Main()
