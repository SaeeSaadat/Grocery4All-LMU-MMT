from typing import Optional
from database_manager import product as product_db


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
        product_dict = product_db.get_product_with_id(product_id)
        if product_dict is None:
            return None
        return Product(
            product_dict['name'],
            product_dict['purchase_price'],
            product_dict['selling_price'],
            product_id=product_dict['product_id']
        )
