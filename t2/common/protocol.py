import ast

GAME_EVENT = {
    'CREATE_PLAYER': 1
}

RESPONSE_EVENT = {
    'OK': 200,
    'ERROR': 400
}

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
