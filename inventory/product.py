import logging
from typing import Optional, List, Tuple
from database_manager import product as product_db
from database_manager import transactions as transaction_db
from inventory.Exceptions import NotEnoughProductInStock
from inventory.transactions import Transaction, SellTransaction, RestockTransaction, AddTransaction


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

    @staticmethod
    def get_all_products(only_available: bool = False) -> List['Product']:
        """
        This static method is used to retrieve all the products from the database.
        :param only_available: if True, only available products will be returned
        :return: list of products
        """
        return product_db.get_all_products(only_available)

    def add_to_database(self):
        self.product_id = product_db.add_product_to_database(self)  # Register the product in the database
        AddTransaction(self).save_to_database()  # Register the transaction in the database

    def restock(self, quantity: int):
        self.quantity += quantity
        # Register the quantity change in the database
        product_db.update_product_quantity_in_inventory(self.product_id, self.quantity)
        # Register the transaction in the database
        RestockTransaction(self, quantity, value=quantity * self.purchase_price).save_to_database()

    def sell(self, quantity: int):
        if quantity > self.quantity:  # Check if the transaction is possible
            logging.warning("Not enough product in stock to sell %d units of %s", quantity, self.name)
            raise NotEnoughProductInStock
        self.quantity -= quantity

        # Register the quantity change in the database
        product_db.update_product_quantity_in_inventory(self.product_id, self.quantity)
        # Register the transaction in the database
        SellTransaction(self, quantity, value=quantity * self.selling_price).save_to_database()

    def get_transactions(self) -> List[Transaction]:
        return transaction_db.get_all_product_transactions(self)

    def get_inventory_value(self) -> float:
        """
        This method will return how much the available product in the inventory is worth.
        :return: quantity * selling_price
        """
        return self.quantity * self.selling_price

    def get_how_many_sold(self) -> int:
        return transaction_db.get_product_sold_count(self.product_id)

    def get_sold_value(self) -> float:
        return transaction_db.get_product_sold_value(self.product_id)

    def get_how_many_purchased(self) -> int:
        return transaction_db.get_product_purchased_count(self.product_id)

    def get_purchased_value(self) -> float:
        return transaction_db.get_product_purchased_value(self.product_id)

    def get_total_balance(self) -> float:
        """
        This will calculate how much money has been spent buying (restocking) the product
        vs how much profit has been made by selling the product.
        :return: total money spent - total money gained by selling the product
        """
        return self.get_sold_value() - self.get_purchased_value()

    def get_full_description(self, show_zero_quantity: bool = True) -> str:
        description = f"#{self.product_id}: {self.name}\n"
        if self.quantity > 0 or show_zero_quantity:
            description += f"\tQuantity: {self.quantity}\n"
        description += f"\tPurchase Price: {self.purchase_price}\n"
        description += f"\tSelling Price: {self.selling_price}\n"
        description += f"\tTotal Number Of Units Sold: {self.get_how_many_sold()}\n"
        description += f"\tTotal Number Of Units Purchased: {self.get_how_many_purchased()}\n"
        description += f"\tTotal Profit: {self.get_sold_value()}\n"
        description += f"\tTotal Purchase Cost: {self.get_purchased_value()}\n"
        description += f"\tTotal Balance: {self.get_purchased_value()}"
        return description
