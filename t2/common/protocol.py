import ast

SERVER_EVENT = {
    'CREATE_PLAYER': 1
}

CLIENT_EVENT = {
    'CREATE_PLAYER': 1
}

def encode(action, data):
    data['command'] = action;
    return str(data)

def decode(message):
    data = ast.literal_eval(message)

    command = data['command'];
    data.pop('command', None)

    return (command, data)
