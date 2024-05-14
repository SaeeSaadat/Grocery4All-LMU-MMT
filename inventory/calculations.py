"""
This module is used to implement the calculations of the calculator mode.
"""
from database_manager import transactions
from inventory.product import Product
from inventory.transactions import RestockTransaction, SellTransaction


def calculate_total_value() -> float:
    value = 0.0
    for product in Product.get_all_products(True):
        value += product.get_inventory_value()

    return value


def calculate_total_revenue() -> float:
    """
        This function calculates the total profit of the inventory.
        These revenues have been calculated by summing up the total value of all the sell transactions.
        :return:
        """
    revenue = 0.0
    for transaction in SellTransaction.get_recent_transactions(None):
        revenue += transaction['total_value']
    return revenue


def calculate_total_cost() -> float:
    """
    This function calculates the total cost of the inventory.
    These costs have been calculated by summing up the total value of all the restock transactions.
    :return:
    """
    cost = 0.0
    for transaction in RestockTransaction.get_recent_transactions(None):
        cost += transaction['total_value']
    return cost


def calculate_total_profit() -> float:
    """
    This function calculates the total profit of the inventory.
    It is calculated by the total revenue minus the total cost.
    :return:
    """
    revenue: float = 0.0
    for transaction in transactions.get_transaction_values():
        total_value = transaction['total_value'] or 0
        if transaction['type'] == 'Restock':
            total_value *= -1
        revenue += total_value
    return revenue
