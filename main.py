import os
from sys import platform

def clear_console():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

clear_console()


avaliable_commands = ["quit", "clear", "help", "pyos", "pyos --version", ""]

while True:
    command = input("[usr@pyos] : ")
    if command in avaliable_commands:
        if command == "help":
            print("quit - exit the terminal.")
            print("clear - clear console.")
        if command == "clear":
            clear_console()
        if command == "quit":
            exit()         
        if command == "":
            print()
        if command == "pyos":
            print("pyos terminal, made by cheor 2023.")
        if command == "pyos --version":
            print("pyos 1")

    if command not in avaliable_commands:
        print("'" + command + "'" + " is not recognized as a command.")