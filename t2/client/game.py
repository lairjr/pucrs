import commands
import player_state

PlayerState = player_state.PlayerState.get_instance()

commands_handler = {
    "tips" : commands.tips,
    "move" : commands.move,
    "list objects" : commands.list_objects
}

def initialize():
    server_ip = raw_input("Inform the server ip: ")
    PlayerState.set_server_ip(server_ip)
    print("Welcome to the game!")
    commands.player_initialize()

def main_loop():
    message = raw_input("command: ")

    while message != "exit":
        commands_handler[message]();
        message = raw_input("command: ")

    print("Bye!")

def run():
    initialize()

    main_loop()
