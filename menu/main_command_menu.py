from menu.command_menu import CommandMenu
import database_manager


class MainCommandMenu(CommandMenu):
    def handle_custom_commands(self, command: str):
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
        elif command == "Calculator":
            print("Entering Calculator mode")
        elif command == "mock data":
            # Fills the database with mock data, using the database_manager/mock_data.sql script.
            database_manager.insert_mock_data()
