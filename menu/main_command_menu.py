from menu.command_menu import CommandMenu
from menu.calculator_command_menu import CalculatorCommandMenu
import database_manager


class MainCommandMenu(CommandMenu):
    commands = {
        "inventory",
        "products",
        "new product",
        "sell",
        "restock",
        "history",
        "calculator",
        "mock data",
    }
    help_menu_file = 'resources/help_message.txt'  # Address of the text file containing relevant instructions!

    def handle_custom_commands(self, command: str) -> CommandMenu:
        if command == "inventory":
            print("TODO: Inventory")
        elif command == "products":
            print("Show products")
        elif command == "new product":
            print("add prd")
        elif command == "sell":
            pass
        elif command == "restock":
            pass
        elif command == "history":
            print("History")
        elif command == "calculator":
            print("Entering Calculator mode")
            return CalculatorCommandMenu(self)
        elif command == "mock data":
            # Fills the database with mock data, using the database_manager/mock_data.sql script.
            database_manager.insert_mock_data()

        return self
