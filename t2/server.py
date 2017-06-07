import socket

def Main():
    out_string = ""
    # set up host on my own computer
    host = socket.gethostname()
    port = 5002
    #create socket obj
    s = socket.socket()
    # bind socket to port @ host, port
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()
    while True:
        data = c.recv(1024)
        out_file = open("Client_Data.txt", "w")
        out_string += str(data)
        out_string += "\n"
        out_file.write(out_string)
        if not data:
            break

        print(str(data))
        c.send(" Wubalabadubdub!!!!")
    s.close()

if __name__ == '__main__':
        Main()
