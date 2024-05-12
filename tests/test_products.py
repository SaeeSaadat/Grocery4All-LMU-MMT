import unittest
import os

import database_manager
from database_manager import product as product_db


class TestProducts(unittest.TestCase):

    def setUp(self):
        database_manager.initialize_database('test_database.sqlite', delete_previous_db=True)
        database_manager.insert_mock_data()

    def tearDown(self):
        os.remove('database_manager/test_database.sqlite')

    def test_mock_data(self):
        self.assertTrue(os.path.exists('database_manager/test_database.sqlite'))
        self.assertEqual(product_db.get_product_by_id(1).name, 'Milk')
        self.assertEqual(product_db.get_product_by_id(10).name, 'Coffee Beans')
        self.assertEqual(product_db.get_product_by_id(5).quantity, 480)

    def test_get_all_products(self):
        products = product_db.get_all_products()
        self.assertEqual(len(products), 13)
        self.assertEqual(products[0].name, 'Milk')
        self.assertEqual(products[9].name, 'Coffee Beans')
        products = product_db.get_all_products(only_available=True)
        self.assertEqual(len(products), 10)
