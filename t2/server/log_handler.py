import os

LOG_FILE = "log.txt"

def clear():
    if os.path.isfile(LOG_FILE):
        os.remove(LOG_FILE)

def log(message):
    out_file = open("log.txt", "a+")
    out_string = str(message)
    out_string += "\n"
    out_file.write(out_string)
