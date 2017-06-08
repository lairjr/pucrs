import common.socket_handler
import log_handler

handler = common.socket_handler.SocketHandler.get_instance()

def initialize():
    log_handler.clear()

    port = 5002

    handler.connect('', port)

    print("Welcome to the server!")

def main_loop():
    while True:
        print("Waiting to receive commands...")
        message, received_address = handler.receivefrom()

        log_handler.log(message)
        if not message:
            break

        print(str(message))
        handler.sendto(" Wubalabadubdub!!!!", received_address)
    handler.close()

def run():
    initialize()

    main_loop()
