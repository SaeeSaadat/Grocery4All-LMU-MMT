import unittest
from menu import main_command_menu


class TestMenus(unittest.TestCase):
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
