class DatabaseAlreadyExistsException(Exception):
    def __init__(self, inventory_name: str):
        super().__init__(f"The database already exists for {inventory_name}!")
        self.inventory_name = inventory_name
