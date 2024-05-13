from typing import List

from inventory.product import Product
from database_manager import transactions as transaction_db


class Transaction:
    """
    This class represents a transaction. It is an abstract class.
    """

    def __init__(self, product: Product):
        self.product = product

    def add_to_database(self):
        raise Exception("Not Implemented in the subclass!")


class SaleTransaction(Transaction):
    """
    This class represents a sale transaction.
    """

    def __init__(self, product: Product, quantity: int):
        super().__init__(product)
        self.quantity = quantity

    def __str__(self):
        return f"Sale Transaction: {self.quantity} units of product #{self.product.product_id}"

    def add_to_database(self):
        transaction_db.save_transaction_to_database('Sale', self.product.product_id, self.quantity)


class RestockTransaction(Transaction):
    """
    This class represents a restock transaction.
    """

    def __init__(self, product: Product, quantity: int):
        super().__init__(product)
        self.quantity = quantity

    def __str__(self):
        return f"Restock Transaction: {self.quantity} units of product #{self.product.product_id}"

    def add_to_database(self):
        transaction_db.save_transaction_to_database('Restock', self.product.product_id, self.quantity)


class AddTransaction(Transaction):
    """
    This class represents an add transaction.
    """

    def __init__(self, product: Product):
        super().__init__(product)

    def __str__(self):
        return f"Add Transaction: Product {self.product.name} -> #{self.product.product_id}"

    def add_to_database(self):
        transaction_db.save_transaction_to_database('Add', self.product.product_id)
