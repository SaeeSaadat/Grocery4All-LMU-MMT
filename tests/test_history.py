import os
import unittest
import database_manager
from database_manager import history


class TestHistory(unittest.TestCase):

    def setUp(self):
        database_manager.initialize_database('test_database.sqlite', delete_previous_db=True)

    def tearDown(self):
        os.remove('database_manager/test_database.sqlite')

    def test_history(self):
        history.record_command('test command 1')
        history.record_command('test command 2')
        history.record_command('test command 3')
        history.record_command('test command 4')

        self.assertEqual(history.get_history(2), ['test command 4', 'test command 3'])
        self.assertEqual(len(history.get_history()), 4)
        history.record_command('test command 5')
        self.assertEqual(len(history.get_history()), 5)
        self.assertEqual(len(history.get_history(2)), 2)

        for _ in range(10):
            history.record_command('test command X')
        self.assertEqual(len(history.get_history()), 10)
        self.assertEqual(len(history.get_history(15)), 15)
