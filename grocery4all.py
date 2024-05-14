import logging
from utilities import print_message, clear_terminal, get_valid_input
import database_manager
from database_manager.Exceptions import DatabaseAlreadyExistsException
from menu.main_command_menu import MainCommandMenu


def configure_logging():
    logging.basicConfig(
        filename='logs/grocery4all.log',
        # level=logging.INFO,
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def setup():
    """
    This function is responsible for setting up the program.
    It will do the configurations of the software, as well as setting up the database.
    :return: The inventory object, which is used to access the data of the inventory.
    """
    clear_terminal()
    configure_logging()
    print_message('resources/welcome_message.txt')
    try:
        database_manager.initialize_database()
        inventory_name = get_valid_input("Welcome to your brand new inventory! What should we name it?  > ")
        database_manager.setup_inventory(inventory_name)
    except DatabaseAlreadyExistsException as e:
        print(f"\nWelcome back to {e.inventory_name}!\n\n")


def graceful_exit():
    print_message('resources/exit_message.txt')


def start():
    menu = MainCommandMenu()
    try:
        while True:
            print(f'\n[ {menu.get_path_to_menu()} ]')
            command = input("  > \t").lower()
            if command == "exit":
                logging.warning("Exiting the program by user's request!")
                graceful_exit()
                break
            elif command:
                menu = menu.handle_command(command)

    except KeyboardInterrupt:
        graceful_exit()


if __name__ == '__main__':
    setup()
    start()
