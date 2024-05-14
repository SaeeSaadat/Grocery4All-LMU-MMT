from typing import List

from inventory import inventory, product_manager
from menu.command_menu import CommandMenu
from menu.calculator_command_menu import CalculatorCommandMenu
import database_manager
from database_manager import history as history_db
from utilities import print_warning


class MainCommandMenu(CommandMenu):
    commands = {
        "inventory",
        "products",
        "add",
        "sell",
        "restock",
        "history",
        "calculator",
        "mock",
    }
    menu_name = "Main Menu"
    help_menu_file = 'resources/help_message.txt'  # Address of the text file containing relevant instructions!

    def handle_custom_commands(self, command: str, arguments: List[str]) -> CommandMenu:
        if command == "inventory":
            print(inventory.get_inventory_info_string())
        elif command == "products":
            print(inventory.get_inventory_products_list_string())
        elif command == "add":
            try:
                product_manager.add_product_sequence()
            except KeyboardInterrupt:
                # Each sequence can be cancelled using ctrl+c
                print_warning("Add Operation Cancelled!")
        elif command == "sell":
            try:
                product_manager.sell_product_sequence()
            except KeyboardInterrupt:
                print_warning("Sell Operation Cancelled!")
        elif command == "restock":
            pass
        elif command == "history":
            MainCommandMenu.show_history(arguments)
        elif command == "calculator":
            print_warning("Entering Calculator Mode")
            return CalculatorCommandMenu(self)
        elif command == "mock":
            database_manager.insert_mock_data()

        return self

    @staticmethod
    def show_history(arguments):
        print("\nYour command history: \n----------------------------------------\n")
        limit = 10
        if len(arguments) > 0 and arguments[0].isdigit() and int(arguments[0]) > 0:
            limit = int(arguments[0])
        for command in history_db.get_history(limit, include_timestamp=True):
            print(f'{command[1]}: \t {command[0]}')
        print("\n----------------------------------------\n")
