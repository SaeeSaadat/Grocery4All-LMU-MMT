import unittest
import os

import database_manager
from inventory.product import Product
from inventory.transactions import Transaction, SellTransaction
from inventory import calculations


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
            quantity=0
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
        # Adding a product with quantity 0 should not trigger a restock transaction
        self.assertEqual(0,
                         len(
                             list(
                                 filter(
                                     lambda x: x.__class__.__name__ == 'RestockTransaction',
                                     new_product.get_transactions()
                                 )
                             )
                         )
                         )

    def test_add_and_restock_product(self):
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
        # Adding a product with quantity more than 0 should trigger a restock transaction
        self.assertEqual(1,
                         len(
                             list(
                                 filter(
                                     lambda x: x.__class__.__name__ == 'RestockTransaction',
                                     new_product.get_transactions()
                                 )
                             )
                         )
                         )

    def test_restock_product(self):
        product = Product.get_product_from_database(1)
        initial_quantity = product.quantity
        product.restock(100)
        product.restock(10)
        self.assertEqual(3,
                         len(
                             list(
                                 filter(
                                     lambda x: x.__class__.__name__ == 'RestockTransaction', product.get_transactions()
                                 )
                             )
                         )
                         )
        self.assertEqual(product.get_purchased_value(), (initial_quantity + 110) * product.purchase_price)

    def test_sell_product(self):
        product = Product.get_product_from_database(1)
        product.sell(100)
        self.assertEqual(1,
                         len(
                             list(
                                 filter(
                                     lambda x: x.__class__.__name__ == 'SellTransaction', product.get_transactions()
                                 )
                             )
                         )
                         )
        self.assertEqual(product.get_sold_value(), 100 * product.selling_price)

    def test_transaction_history(self):
        prv_len = len(Transaction.get_recent_transactions(100))
        product = Product.get_product_from_database(1)
        product.restock(10)
        product.sell(5)
        product = Product.get_product_from_database(2)
        product.restock(10)
        product.sell(5)
        self.assertEqual(len(Transaction.get_recent_transactions(100)), prv_len + 4)
        self.assertEqual(len(SellTransaction.get_recent_transactions(100)), 2)

    def test_product_revenue(self):
        product = Product.get_product_from_database(1)
        stock_value = product.get_purchased_value()
        product.restock(10)
        product.sell(5)
        expected_balance = 5 * product.selling_price - (stock_value + 10 * product.purchase_price)
        self.assertEqual(product.get_total_profit(), expected_balance)

    def test_inventory_profit(self):
        initial_value = calculations.calculate_total_profit()
        product = Product.get_product_from_database(1)
        product.restock(1)
        product.sell(5)
        self.assertEqual(calculations.calculate_total_profit(),
                         initial_value + 5 * product.selling_price - product.purchase_price)
        initial_value = calculations.calculate_total_profit()
        product = Product.get_product_from_database(2)
        product.restock(6)
        product.sell(6)
        self.assertEqual(calculations.calculate_total_profit(),
                         initial_value + 6 * product.selling_price - product.purchase_price * 6)

    def test_inventory_value(self):
        initial_value = calculations.calculate_total_value()
        product = Product.get_product_from_database(1)
        product.restock(1)
        self.assertEqual(calculations.calculate_total_value(), initial_value + product.purchase_price)
        initial_value = calculations.calculate_total_value()
        product = Product.get_product_from_database(2)
        product.restock(6)
        self.assertEqual(calculations.calculate_total_value(), initial_value + product.purchase_price * 6)
        initial_value = calculations.calculate_total_value()
        product = Product('ketchup', 100.0, 2.0, quantity=0)
        product.add_to_database()
        product.restock(100)
        product.sell(1)
        self.assertEqual(calculations.calculate_total_value(), initial_value + 100 * 99)

    def test_inventory_total_cost(self):
        initial_cost = calculations.calculate_total_cost()
        product = Product.get_product_from_database(1)
        product.restock(1)
        self.assertEqual(calculations.calculate_total_cost(), initial_cost + product.purchase_price)
        initial_cost = calculations.calculate_total_cost()
        product = Product.get_product_from_database(2)
        product.restock(6)
        product.sell(1)
        self.assertEqual(calculations.calculate_total_cost(), initial_cost + product.purchase_price * 6)
        initial_cost = calculations.calculate_total_cost()
        product = Product('ketchup', 100.0, 2.0, quantity=0)
        product.add_to_database()
        product.restock(100)
        self.assertEqual(calculations.calculate_total_cost(), initial_cost + 100 * 100)

    def test_total_revenue(self):
        initial_revenue = calculations.calculate_total_revenue()
        product = Product.get_product_from_database(1)
        product.restock(10)
        product.sell(1)
        self.assertEqual(calculations.calculate_total_revenue(), initial_revenue + product.selling_price)
        initial_revenue = calculations.calculate_total_revenue()
        product = Product.get_product_from_database(2)
        product.sell(6)
        self.assertEqual(calculations.calculate_total_revenue(), initial_revenue + product.selling_price * 6)
        initial_revenue = calculations.calculate_total_revenue()
        product = Product('ketchup', 10.0, 20.0, quantity=0)
        product.add_to_database()
        product.restock(100)
        product.sell(100)
        self.assertEqual(calculations.calculate_total_revenue(), initial_revenue + 20 * 100)
