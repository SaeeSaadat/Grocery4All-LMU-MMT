from database_manager import _get_connection_and_cursor
from typing import Optional
from inventory.product import Product
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


def save_product_to_database(product: Product):
    with _get_connection_and_cursor(commit=True) as (conn, cursor):
        cursor.execute("INSERT INTO products (name, purchase_price, selling_price) VALUES (?, ?, ?)",
                       (product.name, product.purchase_price, product.selling_price))
        logging.info("Saved new product object %s to the database", product.name)


def update_product_quantity_in_inventory(product_id: int, quantity: int):
    with _get_connection_and_cursor(commit=True) as (conn, cursor):
        cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (quantity, product_id))

        logging.info("Updated the quantity of product #%d in the inventory to value %d", product_id, quantity)


def get_all_products(only_available: bool = False) -> list[Product]:
    with _get_connection_and_cursor(return_dict=True) as (conn, cursor):
        if only_available:
            cursor.execute(
                "SELECT * FROM products WHERE quantity > 0;")
        else:
            cursor.execute("SELECT * FROM products;")
        products = cursor.fetchall()
        return [Product(
            product['name'],
            product['purchase_price'],
            product['selling_price'],
            product_id=product['id'],
            quantity=product['quantity']
        ) for product in products]
