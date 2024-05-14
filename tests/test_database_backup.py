import os
import unittest
import database_manager
from database_manager import history


class TestDatabaseBackup(unittest.TestCase):

    def setUp(self):
        database_manager.initialize_database('test_database.sqlite', delete_previous_db=True)

    def tearDown(self):
        os.remove('database_manager/test_database.sqlite')

    def test_backup(self):
        history.record_command('test command 1')
        history.record_command('test command 2')
        database_manager.backup_database()
        self.assertEqual(os.path.exists('database_manager/test_database.sqlite.backup'), True)
        os.remove('database_manager/test_database.sqlite.backup')

    def test_reset(self):
        history.record_command('test command 1')
        history.record_command('test command 2')
        database_manager.reset_database()
        self.assertEqual(history.get_history(), [])
        self.assertEqual(os.path.exists('database_manager/test_database.sqlite'), True)
        self.assertEqual(os.path.exists('database_manager/test_database.sqlite.backup'), True)
        os.remove('database_manager/test_database.sqlite.backup')


    def test_restore(self):
        history.record_command('test command 1')
        history.record_command('test command 2')
        database_manager.reset_database()
        self.assertEqual(history.get_history(), [])
        database_manager.restore_database()
        self.assertEqual(history.get_history(), ['test command 2', 'test command 1'])
        database_manager.restore_database()
        self.assertEqual(history.get_history(), [])

        os.remove('database_manager/test_database.sqlite.backup')
