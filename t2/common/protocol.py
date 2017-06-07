ACTIONS = {
    'CREATE_PLAYER': 1
}

def actions():
    return ACTIONS

def encode(action, data):
    data['command'] = action;
    return str(data)
