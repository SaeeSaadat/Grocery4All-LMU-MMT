from typing import Optional
import logging

import utilities
from database_manager import history as history_db


class CommandMenu:
    """
    The user interacts with the software using these menu objects.
    This super class is used and extended by the other menu modules available in the directory.
    This design will significantly help if this project was to be extended and maintained in the future.
    I know it's a bit extra :) But I'm really having fun with this project and thought it'd be a good design.
    """

    commands = {'help, clear'}  # Set of available commands for the menu.
    help_menu_file = 'resources/help_message.txt'  # Address of the text file containing relevant instructions!

    @staticmethod
    def record_command_in_history(command: str):
        logging.debug("Command:  %s", command)
        history_db.record_command(command)

    def __init__(self, prv_menu: Optional['CommandMenu'] = None):
        self.prv_menu = prv_menu

    def __str__(self):
        return f'Menu {self.__class__}'

    def show_help(self):
        utilities.print_message(self.__class__.help_menu_file)

    def handle_custom_commands(self, command: str) -> 'CommandMenu':
        raise Exception("handle_custom_commands method is not implemented!")

    def handle_command(self, command: str) -> 'CommandMenu':
        """
        Do not override this method.
        It will call the `handle_custom_commands` method, which should be overriden in each subclass.
        It will handle commands common between all menus, and then calls the handle_custom_commands method.
        :param command: the command in question!
        :return: the next menu for the next command.
        """

        if command == 'back':
            if self.prv_menu is None:
                print("You're in the first page!")
                logging.warning("User tried to go back in menu %s but there was no prv menu!", self)
            else:
                logging.debug("user returned to previous menu: %s", self.prv_menu)
                print("Going back to", self.prv_menu)
                return self.prv_menu
        elif command == 'clear':
            utilities.clear_terminal()
        elif command == 'help':
            self.show_help()
        elif command not in self.commands:
            print("Command not recognized.")
            logging.warning("Command %s not recognized", command)
        else:
            return self.handle_custom_commands(command)

        return self
