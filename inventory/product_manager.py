"""
This module holds all the methods related to the management of products.
"""
import logging

from inventory.product import Product
from inventory.Exceptions import NotEnoughProductInStock, ProductExistsInDatabase
from inventory.transactions import RestockTransaction
from utilities import print_warning, get_red_string


def add_product_sequence():
    """
    This function will guide the user through the process of adding a product to the inventory.
    :return:
    """
    print("Please enter the following information to add a product to the inventory:")
    name = input("Product Name: ")
    purchase_price = float(input("Purchase Price: "))
    selling_price = float(input("Selling Price: "))
    quantity = input("Quantity (Default = 0): ")
    quantity = int(quantity) if quantity != "" else 0

    new_product = Product(name=name, purchase_price=purchase_price, selling_price=selling_price, quantity=quantity)
    try:
        transaction = new_product.add_to_database()
    except ProductExistsInDatabase:
        print_warning(f"Product with name {new_product.name} already exists in the inventory.")
        return
    if quantity > 0:
        print(f"{quantity} Units of product {new_product.name} added to the inventory.")
        if isinstance(transaction, RestockTransaction):
            print(f"Transaction ID: {transaction.transaction_id}")
            print(f"Total Value: {transaction.value}")
    else:
        print(f"Product {new_product.name} added to the inventory.")


def sell_product_sequence():
    """
    This function will guide the user through the process of selling a product from the inventory.
    :return:
    """
    print("Please enter the following information to sell a product from the inventory:")
    product_id = int(input("Product ID: "))
    product = Product.get_product_from_database(product_id)
    if product is None:
        print(f"Product with ID {product_id} not found in the inventory.")
        return
    else:  # Product found in the inventory
        print(f"Target Product:\t {get_red_string(product.name)}")
        print("If this is not the product you want to sell, please cancel the operation using ctrl+c.")
        quantity = 0
        while quantity <= 0:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Please provide a positive quantity!")
    try:
        transaction = product.sell(quantity)
        print(f"{quantity} Units of product {product.name} sold.")
        print(f"Transaction ID: {transaction.transaction_id}")
        print(f"Total Value: {transaction.value}")
    except NotEnoughProductInStock:
        print(f"Cannot sell {quantity} units of {product.name}. Not enough in stock.")


def restock_product_sequence():
    """
    This function will guide the user through the process of restocking a product in the inventory.
    :return:
    """
    print("Please enter the following information to restock a product in the inventory:")
    product_id = int(input("Product ID: "))
    product = Product.get_product_from_database(product_id)
    if product is None:
        print(f"Product with ID {product_id} not found in the inventory.")
        return
    else:  # Product found in the inventory
        print(f"Target Product:\t {get_red_string(product.name)}")
        print("If this is not the product you want to restock, please cancel the operation using ctrl+c.")
        quantity = 0
        while quantity <= 0:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Please provide a positive quantity!")
    transaction = product.restock(quantity)
    print(f"{quantity} Units of product {product.name} restocked.")
    print(f"Transaction ID: {transaction.transaction_id}")
    print(f"Total Value: {transaction.value}")
