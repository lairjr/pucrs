import socket

s = ''

def initialize(host, port):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host,port))

def send(message):
    global s
    s.send(message)

def receive():
    global s
    return s.recv(1024)

def close():
    global s
    s.close()
