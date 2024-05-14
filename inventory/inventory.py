from typing import Optional

from inventory.product import Product
from inventory.transactions import Transaction
from database_manager import get_inventory_name


def get_inventory_info_string() -> str:
    result = f"\nInventory Name:\t {get_inventory_name()}\n\t--------------------\n\n"
    result += get_inventory_products_list_string(True)
    return result


def get_inventory_products_list_string(only_available: bool = False) -> str:
    all_products = Product.get_all_products(only_available)
    result = "Available Products:\n\n"
    for prd in filter(lambda x: x.quantity > 0, all_products):
        result += prd.get_full_description(show_zero_quantity=False) + "\n"
    if only_available:
        return result
    result += "\n--------------------\n\nOut of Stock Products:\n\n"
    for prd in filter(lambda x: x.quantity == 0, all_products):
        result += prd.get_full_description(show_zero_quantity=False) + "\n"
    return result


def get_inventory_transactions_list_string(limit: Optional[int] = 10) -> str:
    result = "\nRecent Transactions: \n----------------------------------------\n"
    # for transaction in transactions.get_transactions(limit=limit):
    for transaction in Transaction.get_recent_transactions(limit=limit)[::-1]:
        transaction_info = f'{transaction["id"]}: {transaction["type"]} Transaction: '
        if transaction["type"] in ['Sell', 'Restock']:
            transaction_info += f'\n\t{transaction["quantity"]} units of product #{transaction["product_id"]}'
            transaction_info += f'\n\tTotal Value: {transaction["total_value"]}$'
        elif transaction["type"] == 'Add':
            transaction_info += f'\tProduct #{transaction["product_id"]}'
        else:
            transaction_info += f'Unknown Transaction Type: {transaction["type"]}'
        result += transaction_info + "\n"
    result += "\n----------------------------------------\n"

    return result
