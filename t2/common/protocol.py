import ast

ACTIONS = {
    'CREATE_PLAYER': 1
}

def actions():
    return ACTIONS

def encode(action, data):
    data['command'] = action;
    return str(data)

def decode(message):
    data = ast.literal_eval(message)
    
    command = data['command'];
    data.pop('command', None)

    return (command, data)
