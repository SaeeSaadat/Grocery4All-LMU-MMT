from inventory.product import Product as ProductClass
from database_manager import get_inventory_name


def get_inventory_info_string() -> str:
    result = f"\nInventory Name:\t {get_inventory_name()}\n\t--------------------\n\n"
    result += get_inventory_products_list_string(True)
    return result


def get_inventory_products_list_string(only_available: bool = False) -> str:
    all_products = ProductClass.get_all_products(only_available)
    result = "Available Products:\n\n"
    for prd in filter(lambda x: x.quantity > 0, all_products):
        result += prd.get_full_description(show_zero_quantity=False) + "\n"
    if only_available:
        return result
    result += "\n--------------------\n\nOut of Stock Products:\n\n"
    for prd in filter(lambda x: x.quantity == 0, all_products):
        result += prd.get_full_description(show_zero_quantity=False) + "\n"
    return result
