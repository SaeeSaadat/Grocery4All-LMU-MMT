"""
This module holds all the methods related to the management of products.
"""
from inventory.product import Product


def add_product_sequence():
    """
    This function will guide the user through the process of adding a product to the inventory.
    :return:
    """
    print("Please enter the following information to add a product to the inventory:")
    name = input("Product Name: ")
    purchase_price = float(input("Purchase Price: "))
    selling_price = float(input("Selling Price: "))
    quantity = int(input("Quantity (Default = 0): "))

    new_product = Product(name=name, purchase_price=purchase_price, selling_price=selling_price, quantity=quantity)
    new_product.add_to_database()
    print(f"{quantity} Units of product {new_product.name} added to the inventory.")
