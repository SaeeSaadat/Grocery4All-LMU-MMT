from database_manager import transactions as transaction_db


class Transaction:
    """
    This class represents a transaction. It is an abstract class.
    """

    def __init__(self, product):
        self.product = product

    def save_to_database(self):
        raise Exception("Not Implemented in the subclass!")


class SellTransaction(Transaction):
    """
    This class represents a sell transaction.
    """

    def __init__(self, product, quantity: int, value: float):
        super().__init__(product)
        self.quantity = quantity
        self.value = value
        # The reason we save the value in the database instead of calculating it everytime, is that a transaction might
        # be from a time when the price of the product was different from now!

    def __str__(self):
        return f"Sell Transaction: {self.quantity} units of product #{self.product.product_id}"

    def save_to_database(self):
        transaction_db.save_transaction_to_database('Sell', self.product.product_id, self.quantity)


class RestockTransaction(Transaction):
    """
    This class represents a restock transaction.
    """

    def __init__(self, product, quantity: int, value: float):
        super().__init__(product)
        self.quantity = quantity
        self.value = value

    def __str__(self):
        return f"Restock Transaction: {self.quantity} units of product #{self.product.product_id}"

    def save_to_database(self):
        transaction_db.save_transaction_to_database('Restock', self.product.product_id, self.quantity)


class AddTransaction(Transaction):
    """
    This class represents an add transaction.
    """

    def __init__(self, product):
        super().__init__(product)

    def __str__(self):
        return f"Add Transaction: Product {self.product.name} -> #{self.product.product_id}"

    def save_to_database(self):
        transaction_db.save_transaction_to_database('Add', self.product.product_id)
