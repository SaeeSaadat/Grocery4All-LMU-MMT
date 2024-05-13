import unittest
import os

import database_manager
from database_manager import product as product_db
from inventory.product import Product
from inventory.transactions import Transaction, SellTransaction, AddTransaction, RestockTransaction
from inventory.Exceptions import ProductExistsInDatabase, NotEnoughProductInStock


class TestProducts(unittest.TestCase):

    def setUp(self):
        database_manager.initialize_database('test_database.sqlite', delete_previous_db=True)
        database_manager.insert_mock_data()

    def tearDown(self):
        os.remove('database_manager/test_database.sqlite')

    def test_add_product(self):
        new_product = Product(
            'ketchup',
            1.0,
            2.0,
            quantity=20
        )
        new_product.add_to_database()
        self.assertEqual(1,
                         len(
                             list(
                                 filter(
                                     lambda x: x.__class__.__name__ == 'AddTransaction', new_product.get_transactions()
                                 )
                             )
                         )
                         )

    def test_restock_product(self):
        product = Product.get_product_from_database(1)
        product.restock(100)

    def test_sell_product(self):
        product = Product.get_product_from_database(1)
        product.sell(100)
