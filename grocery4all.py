import os
import logging
from inventory import Inventory
import database_manager
from Exceptions import *


def clear_terminal():
    """
    Clear terminal command for different platforms
    """
    command = "clear"  # Linux and macOS
    if os.name == "nt":  # Windows
        command = "cls"
    os.system(command)


def print_message(text_file: str):
    with open(text_file, 'r') as f:
        message = f.read()
    try:
        print(message.center(os.get_terminal_size().columns))
    except OSError:
        # In some terminal windows (like in the IDE) might happen, because of the .get_terminal_size() function
        print(message)


def configure_logging():
    logging.basicConfig(
        filename='logs/grocery4all.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def setup():
    clear_terminal()
    configure_logging()
    print_message('resources/welcome_message.txt')
    try:
        database_manager.initialize_database()
    except DatabaseAlreadyExistsException:
        print("\nWelcome back!\n\n")


def graceful_exit():
    print_message('resources/exit_message.txt')


def start_instruction_loop():
    inventory_object = Inventory.get_inventory()
    try:
        while True:
            instruction = input("\nCommand> \t")
            if instruction.lower() == "exit":
                graceful_exit()
                break
            elif instruction.lower() == "help":
                print("Help instructions")  # TODO: Add help instructions
            elif instruction.lower() == "clear":
                clear_terminal()
            elif instruction.lower() == "mock data":
                database_manager.insert_mock_data()
            elif instruction.lower() == "TODO":
                print("Starting the program...")
            else:
                print("Instruction not recognized.")
    except KeyboardInterrupt:
        graceful_exit()

if __name__ == '__main__':
    setup()
    start_instruction_loop()
