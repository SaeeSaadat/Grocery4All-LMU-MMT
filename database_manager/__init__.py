"""
This module is in charge of handling the database operations.
No other module should have direct access to the database.
This way, we can easily change the database implementation without affecting the rest of the code.
"""
import os
import sqlite3
import logging
from contextlib import contextmanager
from typing import Optional

from database_manager.Exceptions import DatabaseAlreadyExistsException

DB_FILE_NAME = 'database_manager/database.sqlite'


@contextmanager
def _get_connection_and_cursor(commit: bool = False, return_dict: bool = False):
    """
    This function is used to get the connection and cursor objects.
    This method is private and must not be accessed by outside modules.
    :param commit: If true, the connection will automatically commit the changes before closing
    :param return_dict: If true, the results will be in the format of a dictionary instead of tuple
    :return: connection and cursor objects
    """
    conn = sqlite3.connect(DB_FILE_NAME)
    if return_dict:
        conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        yield conn, cursor
    finally:
        if commit:
            conn.commit()
        conn.close()


def initialize_database(db_name: str = 'database.sqlite', delete_previous_db: bool = False):
    """
    This function is used to initialize the database, if and only if the database file doesn't already exist.
    """
    global DB_FILE_NAME

    DB_FILE_NAME = f'database_manager/{db_name}'
    # Check if database file exists
    if os.path.exists(DB_FILE_NAME) and get_inventory_name() is not None:
        if delete_previous_db:
            os.remove(DB_FILE_NAME)
        else:
            raise DatabaseAlreadyExistsException(get_inventory_name())

    # Create the database file
    open(DB_FILE_NAME, 'w').close()

    with _get_connection_and_cursor(True) as (conn, cursor):
        # run the initialize_database.sql script
        with open('database_manager/initiate_database.sql', 'r') as sql_script:
            # Connect to the database
            cursor.executescript(sql_script.read())
            logging.info("Database initialized.")

        # Commit the changes and close the connection
    logging.info("Database initialization completed.")


def insert_mock_data():
    """
    This function is used to insert mock data into the database.
    """
    try:
        with _get_connection_and_cursor(True) as (conn, cursor):
            with open('database_manager/mock_data.sql', 'r') as sql_script:
                cursor.executescript(sql_script.read())
        logging.info("Mock data inserted.")
    except sqlite3.IntegrityError:
        logging.warning("Mock data already exists in the database.")
        print("Mock data already exists in the database.")


def setup_inventory(inventory_name: str):
    with _get_connection_and_cursor(commit=True) as (conn, cursor):
        cursor.execute("INSERT INTO inventory (name) VALUES (?)", (inventory_name,))


def get_inventory_name() -> Optional[str]:
    with _get_connection_and_cursor(True) as (conn, cursor):
        try:
            cursor.execute('SELECT name FROM inventory')
            result = cursor.fetchone()
            return result[0] if result else None
        except sqlite3.OperationalError:
            return None
