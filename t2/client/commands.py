import common.socket_handler
import player_state

PlayerState = player_state.PlayerState.get_instance()
SocketHandler = common.socket_handler.SocketHandler.get_instance()

def player_initialize():
    player_name = raw_input("Give me your player name: ")
    player_data = PlayerState.initialize(player_name)

    message = common.protocol.encode(common.protocol.GAME_EVENT['CREATE_PLAYER'], player_data)
    SocketHandler.sendto(message, ("172.18.0.2", 5002))
    response, received_address = SocketHandler.receivefrom()
    (response_event, data) = common.protocol.decode(response)
    if response_event is not common.protocol.RESPONSE_EVENT['OK']:
        print("Erro ao criar jogador, tente novamente")
        player_initialize()
    PlayerState.update_data(data)

def send():
    SocketHandler.sendto("a", ("172.18.0.2", 5002))
    data = SocketHandler.receivefrom()
    print("received from server: " + str(data))

def tips():
    print("available commands:")
    print("exit - will exit the game;")
    print("tips - will print available commands;")
