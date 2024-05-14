from typing import Optional

from database_manager import transactions as transaction_db


class Transaction:
    """
    This class represents a transaction. It is an abstract class.
    """

    def __init__(self, product, transaction_id: Optional[int] = None):
        self.product = product
        self.transaction_id = transaction_id

    def save_to_database(self):
        raise Exception("Not Implemented in the subclass!")


class SellTransaction(Transaction):
    """
    This class represents a sell transaction.
    """

    def __init__(self, product, quantity: int, value: float, transaction_id: Optional[int] = None):
        super().__init__(product, transaction_id=transaction_id)
        self.quantity = quantity
        self.value = value
        # The reason we save the value in the database instead of calculating it everytime, is that a transaction might
        # be from a time when the price of the product was different from now!

    def __str__(self):
        return f"Sell Transaction: {self.quantity} units of product #{self.product.product_id}"

    def save_to_database(self):
        self.transaction_id = transaction_db.save_transaction_to_database('Sell',
                                                                          self.product.product_id,
                                                                          self.quantity,
                                                                          self.quantity * self.product.selling_price
                                                                          )


class RestockTransaction(Transaction):
    """
    This class represents a restock transaction.
    """

    def __init__(self, product, quantity: int, value: float, transaction_id: Optional[int] = None):
        super().__init__(product, transaction_id=transaction_id)
        self.quantity = quantity
        self.value = value

    def __str__(self):
        return f"Restock Transaction: {self.quantity} units of product #{self.product.product_id}"

    def save_to_database(self):
        self.transaction_id = transaction_db.save_transaction_to_database('Restock',
                                                                          self.product.product_id,
                                                                          self.quantity,
                                                                          self.quantity * self.product.purchase_price
                                                                          )


class AddTransaction(Transaction):
    """
    This class represents an add transaction.
    """

    def __init__(self, product, transaction_id: Optional[int] = None):
        super().__init__(product, transaction_id=transaction_id)

    def __str__(self):
        return f"Add Transaction: Product {self.product.name} -> #{self.product.product_id}"

    def save_to_database(self):
        self.transaction_id = transaction_db.save_transaction_to_database('Add', self.product.product_id)
