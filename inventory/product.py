import logging
from typing import Optional
from database_manager import product as product_db
from inventory.Exceptions import NotEnoughProductInStock
from inventory.transactions import SellTransaction, RestockTransaction, AddTransaction


class Product:
    """
    This class represents a product.
    If it is not in the inventory yet, the quantity will be 0
    """

    def __init__(self, name: str, purchase_price: float, selling_price: float, product_id: Optional[int] = None,
                 quantity: int = 0):
        self.product_id = product_id
        self.name = name
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.quantity = quantity

    def __str__(self):
        return f"Product #{self.product_id}: {self.name}"

    @staticmethod
    def get_product_from_database(product_id: int) -> Optional['Product']:
        """
        This static method is used to retrieve the information of a product from the database using its id
        :param product_id: product id
        :return: the product object, if available in the database, None otherwise.
        """
        return product_db.get_product_by_id(product_id)

    def add_to_database(self):
        self.product_id = product_db.add_product_to_database(self)  # Register the product in the database
        AddTransaction(self).save_to_database()  # Register the transaction in the database

    def restock(self, quantity: int):
        self.quantity += quantity
        # Register the quantity change in the database
        product_db.update_product_quantity_in_inventory(self.product_id, self.quantity)
        RestockTransaction(self, quantity).save_to_database()  # Register the transaction in the database

    def sell(self, quantity: int):
        if quantity > self.quantity:  # Check if the transaction is possible
            logging.warning("Not enough product in stock to sell %d units of %s", quantity, self.name)
            raise NotEnoughProductInStock
        self.quantity -= quantity

        # Register the quantity change in the database
        product_db.update_product_quantity_in_inventory(self.product_id, self.quantity)
        SellTransaction(self, quantity).save_to_database()  # Register the transaction in the database

