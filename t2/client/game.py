import commands
import player

commands = {
    "tips" : commands.tips,
    "send" : commands.send
}

def initialize():
    print("Welcome to the game!")
    player.initialize()

def main_loop():
    message = raw_input("command: ")

    while message != "exit":
        commands[message]();
        message = raw_input("command: ")

    print("Bye!")

def run(host, port):
    initialize()

    main_loop()
