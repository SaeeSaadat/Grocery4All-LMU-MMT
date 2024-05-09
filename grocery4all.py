import os
import logging
from inventory import Inventory
import database_manager


def clear_terminal():
    """
    Clear terminal command for different platforms
    """
    command = "clear"  # Linux and macOS
    if os.name == "nt":  # Windows
        command = "cls"
    os.system(command)


def print_welcome_message():
    with open('welcome_message.txt', 'r') as f:
        welcome_message = f.read()
    try:
        print(welcome_message.center(os.get_terminal_size().columns))
    except OSError:
        # In some terminal windows (like in the IDE) might happen, because of the .get_terminal_size() function
        print(welcome_message)


def configure_logging():
    logging.basicConfig(
        filename='logs/grocery4all.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def setup():
    clear_terminal()
    configure_logging()
    database_manager.initialize_database()
    print_welcome_message()



def graceful_exit():
    print("I hope you come back soon :)\nGoodbye!")
    print("... Developed by: Saee Saadat ...")
    print("... Project GitHub Repository: \t https://github.com/SaeeSaadat/Grocery4All-LMU-MMT ...")
    print("... LinkedIn: \t\t\t https://www.linkedin.com/in/saeesaadat/ ...")


def start_instruction_loop():
    inventory_object = Inventory.get_inventory()
    while True:
        instruction = input("Command> \t")
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


if __name__ == '__main__':
    setup()
    start_instruction_loop()
