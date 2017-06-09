import ast

GAME_EVENT = {
    'CREATE_PLAYER': 1,
    'MOVE_PLAYER': 2
}

RESPONSE_EVENT = {
    'OK': 200,
    'ERROR': 400
}

ETHERNET_PACKET = [
    0x52, 0x54, 0x00, 0x12, 0x35, 0x02, # dst=52:54:00:12:35:02
    0xfe, 0xed, 0xfa, 0xce, 0xbe, 0xef, # src=fe:ed:fa:ce:be:ef
    0x08, 0x00 # type=0x0800 (IP)
]

IPV4_HEADER = [
    0x45, 0x00, #ip version
    0x00, 0x54, #total length
    0x05, 0x9f, #identifier
    0x40, 0x00, #fragment offset
    0x40, #ttl
    0x01, #protocol
    0x2f, 0x93, #checksum
    0x0a, 0x00, 0x02, 0x0f, # src=10.0.2.15
    0xc3, 0x58, 0x36, 0x10 # dst=195.88.54.16
]

UPD_HEADER = [
    0x55, 0x33, #souce port
    0x55, 0x33, #dest port
    0x33, 0x33, #udp length
    0x55, 0x33, #udp checksum
]

def encode(action, data):
    if data is None:
        data = {}
    data['command'] = action;
    return str(data)

def decode(message):
    data = ast.literal_eval(message)

    command = data['command'];
    data.pop('command', None)

    return (command, data)
