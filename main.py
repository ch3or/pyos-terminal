import os
from sys import platform

def clear_console():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

clear_console()


avaliable_commands = ["", "clear", "help", "pyos", "pyos --version", "quit"]

while True:
    command = input("[usr@pyos] : ")
    if command in avaliable_commands:
        if command == "help":
            print("quit - exit the terminal.")
            print("clear - clear console.")
            print("pyos - some details.")
            print("pyos --version - pyos version.")
        if command == "clear":
            clear_console()
        if command == "quit":
            exit()         
        if command == "":
            print()
        if command == "pyos":
            print("pyos terminal, made by cheor 2023.")
        if command == "pyos --version":
            print("pyos v1.0")

    if command not in avaliable_commands:
        print("'" + command + "'" + " is not recognized as a command.")
