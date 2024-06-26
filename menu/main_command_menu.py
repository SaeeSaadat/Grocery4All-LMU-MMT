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
        "transactions",
        "add",
        "sell",
        "restock",
        "history",
        "calculator",
        "mock",
        "backup",
        "reset",
        "restore"
    }
    menu_name = "Main Menu"
    help_menu_file = 'resources/help_message.txt'  # Address of the text file containing relevant instructions!

    def handle_custom_commands(self, command: str, arguments: List[str]) -> CommandMenu:
        if command == "inventory":
            print(inventory.get_inventory_info_string())
        elif command == "products":
            print(inventory.get_inventory_products_list_string())
        elif command == "transactions":
            limit = int(arguments[0]) if len(arguments) > 0 and arguments[0].isdigit() else 10
            print(inventory.get_inventory_transactions_list_string(limit))
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
            try:
                product_manager.restock_product_sequence()
            except KeyboardInterrupt:
                print_warning("Sell Operation Cancelled!")
        elif command == "history":
            MainCommandMenu.show_history(arguments)
        elif command == "calculator":
            print_warning("Entering Calculator Mode")
            return CalculatorCommandMenu(self)
        elif command == "mock":
            database_manager.insert_mock_data()
        elif command == "reset":
            print_warning("This will reset the database and all the data will be lost!")
            try:
                confirm = input("Are you sure you want to reset the database? (yes/no) > ")
                if confirm.lower() == "yes":
                    database_manager.reset_database()
                    print("Database reset successfully!")
                    print("you may restore the previous data using the 'restore' command.")
            except KeyboardInterrupt:
                print("Reset Operation Cancelled!\n")
        elif command == "restore":
            print_warning("This will restore the previous data from the backup!")
            try:
                confirm = input("Are you sure you want to restore the previous data? (yes/no) > ")
                if confirm.lower() == "yes":
                    database_manager.restore_database()
                    print("Database restored successfully!")
            except FileNotFoundError:
                print_warning("No backup file found! Please make sure to create a backup before restoring.")
            except KeyboardInterrupt:
                print("Restore Operation Cancelled!\n")

        return self

    @staticmethod
    def show_history(arguments):
        print("\nYour command history: \n----------------------------------------\n")
        limit = 10
        if len(arguments) > 0 and arguments[0].isdigit() and int(arguments[0]) > 0:
            limit = int(arguments[0])
        for command in history_db.get_history(limit, offset=1, include_timestamp=True)[::-1]:
            print(f'{command[1]}: \t {command[0]}')
        print("\n----------------------------------------\n")
