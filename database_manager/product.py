from database_manager import _get_connection_and_cursor
from typing import Optional
from inventory.product import Product
import logging


def get_product_with_id(product_id: int, inventory_id: Optional[int] = None) -> Optional[dict]:
    """
    Retrieves the product from the database using its id
    :param product_id: primary key in the database, used to identify the product
    :param inventory_id: if the quantity of the product in the inventory is needed, must be provided
    :return: dictionary object containing attributes of the product
    """
    with (_get_connection_and_cursor(return_dict=True) as (conn, cursor)):
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product_data = cursor.fetchone()
        if product_data is None:
            return None
        if inventory_id is None:
            return product_data
        cursor.execute("SELECT * FROM inventory_products WHERE product_id = ? AND inventory_id = ?",
                       (product_id, inventory_id))
        quantity_data = cursor.fetchone()
        if quantity_data is not None:
            quantity = quantity_data.get('quantity', 0)
            product_data.update({'quantity': quantity})
        return product_data


def save_product_to_database(product: Product):
    with _get_connection_and_cursor(commit=True) as (conn, cursor):
        cursor.execute("INSERT INTO products (name, purchase_price, selling_price) VALUES (?, ?, ?)",
                       (product.name, product.purchase_price, product.selling_price))
        logging.info("Saved new product object %s to the database", product.name)


def update_product_quantity_in_inventory(product_id: int, inventory_id: int, quantity: int):
    with _get_connection_and_cursor(commit=True) as (conn, cursor):

        # Check if the data row exists in inventory_product table
        cursor.execute("SELECT * FROM inventory_products WHERE inventory_id = ? AND product_id = ?",
                       (inventory_id, product_id))
        if cursor.fetchone() is not None:
            # Update the row
            cursor.execute("UPDATE inventory_products SET quantity = ? WHERE inventory_id = ? AND product_id = ?",
                           (quantity, inventory_id, product_id))

        cursor.execute("INSERT INTO inventory_products (inventory_id, product_id, quantity) VALUES (?, ?, ?)",
                       (product_id, inventory_id, quantity))
        logging.info("Updated the quantity of product #%d in the inventory to value %d", product_id, quantity)
