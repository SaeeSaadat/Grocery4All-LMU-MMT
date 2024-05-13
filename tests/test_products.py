import unittest
import os

import database_manager
from database_manager import product as product_db
from inventory.product import Product
from inventory.Exceptions import ProductExistsInDatabase


class TestProducts(unittest.TestCase):

    def setUp(self):
        database_manager.initialize_database('test_database.sqlite', delete_previous_db=True)
        database_manager.insert_mock_data()

    def tearDown(self):
        os.remove('database_manager/test_database.sqlite')

    def test_mock_data(self):
        self.assertTrue(os.path.exists('database_manager/test_database.sqlite'))
        self.assertEqual(database_manager.get_inventory_name(), 'Grocery 4 All')
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

    def test_add_product(self):
        new_product = Product(
            'ketchup',
            1.0,
            2.0,
            quantity=20
        )
        new_product.add_to_database()
        # Test Insertion
        self.assertEqual(Product.get_product_from_database(new_product.product_id).name, new_product.name)
        # detect duplicate name!
        self.assertRaises(ProductExistsInDatabase, new_product.add_to_database)

    def test_restock_product(self):
        product = Product.get_product_from_database(1)
        prv_quantity = product.quantity
        product.restock(10)
        self.assertEqual(Product.get_product_from_database(1).quantity, prv_quantity + 10)
        product.restock(100)
        self.assertEqual(Product.get_product_from_database(1).quantity, prv_quantity + 110)
