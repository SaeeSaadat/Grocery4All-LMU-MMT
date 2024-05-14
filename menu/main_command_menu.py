from typing import List

from inventory import inventory
from menu.command_menu import CommandMenu
from menu.calculator_command_menu import CalculatorCommandMenu
import database_manager


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
    help_menu_file = 'resources/help_message.txt'  # Address of the text file containing relevant instructions!

    def handle_custom_commands(self, command: str, arguments: List[str]) -> CommandMenu:
        if command == "inventory":
            print(inventory.get_inventory_info_string())
        elif command == "products":
            print("Show products")
        elif command == "add":
            print("add product")
        elif command == "sell":
            pass
        elif command == "restock":
            pass
        elif command == "history":
            print("History")
        elif command == "calculator":
            print("Entering Calculator Mode")
            return CalculatorCommandMenu(self)
        elif command == "mock":
            # Fills the database with mock data, using the database_manager/mock_data.sql script.
            database_manager.insert_mock_data()

        return self
