import logging
from typing import Optional
from database_manager import product as product_db
from inventory.Exceptions import NotEnoughProductInStock


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
        return product_db.get_product_by_id(product_id)

    def add_to_database(self):
        self.product_id = product_db.add_product_to_database(self)

    def restock(self, quantity: int):
        self.quantity += quantity
        product_db.update_product_quantity_in_inventory(self.product_id, self.quantity)
        # TODO: Transaction

    def sell(self, quantity: int):
        if quantity > self.quantity:
            logging.warning("Not enough product in stock to sell %d units of %s", quantity, self.name)
            raise NotEnoughProductInStock
        self.quantity -= quantity
        product_db.update_product_quantity_in_inventory(self.product_id, self.quantity)
        # TODO: Transaction
