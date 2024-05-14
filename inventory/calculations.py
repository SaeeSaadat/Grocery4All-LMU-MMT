"""
This module is used to implement the calculations of the calculator mode.
"""
from database_manager import transactions
from inventory.product import Product


def calculate_total_revenue() -> float:
    revenue: float = 0.0
    for transaction in transactions.get_transaction_values():
        total_value = transaction['total_value'] or 0
        if transaction['type'] == 'Restock':
            total_value *= -1
        revenue += total_value
    return revenue


def calculate_total_value() -> float:
    value = 0.0
    for product in Product.get_all_products(True):
        value += product.get_inventory_value()

    return value


def calculate_total_cost() -> float:
    # TODO
    pass


def calculate_total_profit() -> float:
    # TODO
    pass
