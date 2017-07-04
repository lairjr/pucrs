import common.socket_handler
import player_state
import common.protocol

PlayerState = player_state.PlayerState.get_instance()
SocketHandler = common.socket_handler.SocketHandler.get_instance()

def player_initialize():
    player_name = raw_input("Give me your player name: ")
    player_data = PlayerState.initialize(player_name)

    message = common.protocol.encode(common.protocol.GAME_EVENT['CREATE_PLAYER'], player_data)
    SocketHandler.sendto(message, ("172.19.0.2", 5002))
    response, received_address = SocketHandler.receivefrom()
    (response_event, data) = common.protocol.decode(response)
    if response_event is not common.protocol.RESPONSE_EVENT['OK']:
        print("Erro ao criar jogador, tente novamente")
        player_initialize()
    PlayerState.update_data(data)

def list_objects():
    message = common.protocol.encode(common.protocol.GAME_EVENT['LIST_OBJECTS'], {})
    SocketHandler.sendto(message, ("172.19.0.2", 5002))
    response, received_address = SocketHandler.receivefrom()
    (response_event, data) = common.protocol.decode(response)
    if response_event is not common.protocol.RESPONSE_EVENT['OK']:
        print("Erro ao listar objetos")
    print("Lista objetos:")
    for obj in data["objects"]:
        print(obj["name"])

def move():
    direction = raw_input("(w, s, a ,d): ")
    player_data = PlayerState.move(direction)

    message = common.protocol.encode(common.protocol.GAME_EVENT['MOVE_PLAYER'], player_data)
    SocketHandler.sendto(message, ("172.19.0.2", 5002))
    response, received_address = SocketHandler.receivefrom()
    (response_event, data) = common.protocol.decode(response)
    if response_event is not common.protocol.RESPONSE_EVENT['OK']:
        print("Erro ao move jogador")
    PlayerState.update_data(data)

def tips():
    print("available commands:")
    print("exit - will exit the game;")
    print("list objects - will list all the objects in the room;")
    print("move - will move player in the map;")
    print("tips - will print available commands;")
