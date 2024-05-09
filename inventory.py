from typing import Optional


class Inventory:
    @staticmethod
    def get_inventory() -> 'Inventory':
        """
        SINGLETON!
        This method is used to get the inventory object.
        If the inventory object does not exist, it will create a new one.
        :return: Inventory object
        """
        inventory = Inventory._get_existing_inventory()
        if not inventory:
            inventory = Inventory._create_inventory()
        return inventory

    @staticmethod
    def _get_existing_inventory() -> Optional['Inventory']:
        """
        This method is used to get the existing inventory object from the database.
        :return: Inventory object if it exists, otherwise None
        """
        pass

    @staticmethod
    def _create_inventory() -> 'Inventory':
        """
        This method is used to create a new inventory object.
        It then registers the inventory object in the database.
        :return: Inventory object
        """
        # TODO: Manual Inventory Setup Procedure
        pass

