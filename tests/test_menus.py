import os
import unittest

import database_manager
from menu import main_command_menu


class TestMenus(unittest.TestCase):

    def setUp(self):
        database_manager.initialize_database('test_database.sqlite', delete_previous_db=True)

    def tearDown(self):
        os.remove('database_manager/test_database.sqlite')

    def test_menus(self):
        menu = main_command_menu.MainCommandMenu()
        menu = menu.handle_command('calculator')
        self.assertEqual(menu.__class__.__name__, 'CalculatorCommandMenu')

        menu = menu.handle_command('back')
        self.assertEqual(menu.__class__.__name__, 'MainCommandMenu')
        menu = menu.handle_command('back')
        self.assertEqual(menu.__class__.__name__, 'MainCommandMenu')

        menu = menu.handle_command('nonesensecommand')
        self.assertEqual(menu.__class__.__name__, 'MainCommandMenu')
