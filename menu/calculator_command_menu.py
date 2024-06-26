import logging
from typing import List

from menu.command_menu import CommandMenu
import database_manager
from inventory import calculations


class CalculatorCommandMenu(CommandMenu):
    commands = {
        "revenue",
        "value",
        "cost",
        "profit",
    }
    menu_name = "Calculator"
    help_menu_file = 'resources/calculator_help_message.txt'

    def handle_custom_commands(self, command: str, arguments: List[str]) -> CommandMenu:
        result = 0
        if command == "revenue":
            print("Calculating Total Revenue...")
            result = calculations.calculate_total_revenue()
        elif command == "value":
            result = calculations.calculate_total_value()
        elif command == "cost":
            result = calculations.calculate_total_cost()
        elif command == "profit":
            result = calculations.calculate_total_profit()

        logging.info("Calculation of %s resulted in %f", command, result)
        print(f"The total {command} of the inventory is: \t {result}$")
        return self
