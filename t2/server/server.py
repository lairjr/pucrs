import common2.socket_handler
import sys
import log_handler

handler = common2.socket_handler.SocketHandler.get_instance()

def Main():
    log_handler.clear()

    port = 5002

    handler.connect('', port)

    while True:
        print("waiting to receive messages")
        message, received_address = handler.receivefrom()

        log_handler.log(message)
        if not message:
            break

        print(str(message))
        handler.sendto(" Wubalabadubdub!!!!", received_address)
    handler.close()

if __name__ == '__main__':
        Main()
