import commands
import player_state

PlayerState = player_state.PlayerState.get_instance()

commands = {
    "tips" : commands.tips,
    "send" : commands.send
}

def initialize():
    print("Welcome to the game!")
    PlayerState.initialize()

def main_loop():
    message = raw_input("command: ")

    while message != "exit":
        commands[message]();
        message = raw_input("command: ")

    print("Bye!")

def run():
    initialize()

    main_loop()
