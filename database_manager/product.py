import sqlite3

from database_manager import _get_connection_and_cursor
from typing import Optional
from inventory.product import Product
from inventory.Exceptions import ProductExistsInDatabase
import logging


def get_product_by_id(product_id: int) -> Optional[Product]:
    """
    Retrieves the product from the database using its id
    :param product_id: primary key in the database, used to identify the product
    :return: dictionary object containing attributes of the product
    """
    with _get_connection_and_cursor(return_dict=True) as (conn, cursor):
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product_data = cursor.fetchone()
        if product_data is None:
            return None
        return Product(
            product_data['name'],
            product_data['purchase_price'],
            product_data['selling_price'],
            product_id=product_data['id'],
            quantity=product_data['quantity']
        )


def add_product_to_database(product: Product) -> Optional[int]:
    """
    This function will insert the given product into the database.
    If the product already exists, it will throw an Exception!
    :param product: the product you want to insert into the database!
    :return: ID of the new product.
    """
    with _get_connection_and_cursor(commit=True) as (conn, cursor):
        try:
            cursor.execute("INSERT INTO products (name, purchase_price, selling_price) VALUES (?, ?, ?)",
                           (product.name, product.purchase_price, product.selling_price))
        except sqlite3.IntegrityError as e:
            raise ProductExistsInDatabase from e
        logging.info("Saved new product object %s to the database", product.name)
        return cursor.lastrowid


def update_product_quantity_in_inventory(product_id: int, quantity: int):
    with _get_connection_and_cursor(commit=True) as (conn, cursor):
        cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (quantity, product_id))

        logging.info("Updated the quantity of product #%d in the inventory to value %d", product_id, quantity)


def get_all_products(only_available: bool = False) -> list[Product]:
    with _get_connection_and_cursor(return_dict=True) as (conn, cursor):
        if only_available:
            cursor.execute(
                "SELECT * FROM products WHERE quantity > 0 ORDER BY id;")
        else:
            cursor.execute("SELECT * FROM products ORDER BY id;")
        products = cursor.fetchall()
        return [Product(
            product['name'],
            product['purchase_price'],
            product['selling_price'],
            product_id=product['id'],
            quantity=product['quantity']
        ) for product in products]
