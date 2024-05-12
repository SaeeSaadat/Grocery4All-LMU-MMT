"""
This module is in charge of handling the database operations.
No other module should have direct access to the database.
This way, we can easily change the database implementation without affecting the rest of the code.
"""
import os
import sqlite3
import logging
from contextlib import contextmanager
from database_manager.Exceptions import DatabaseAlreadyExistsException


@contextmanager
def _get_connection_and_cursor(commit: bool = False, return_dict: bool = False):
    """
    This function is used to get the connection and cursor objects.
    This method is private and must not be accessed by outside modules.
    :param commit: If true, the connection will automatically commit the changes before closing
    :param return_dict: If true, the results will be in the format of a dictionary instead of tuple
    :return: connection and cursor objects
    """
    conn = sqlite3.connect('database_manager/database.sqlite')
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
    db_file_name = f'database_manager/{db_name}'
    # Check if database file exists
    if os.path.exists(db_file_name):
        if delete_previous_db:
            os.remove(db_name)
        else:
            raise DatabaseAlreadyExistsException()

    # Create the database file
    open(db_file_name, 'w').close()

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
    with _get_connection_and_cursor(True) as (conn, cursor):
        # TODO: Check if database is not empty!
        with open('database_manager/mock_data.sql', 'r') as sql_script:
            cursor.executescript(sql_script.read())
    logging.info("Mock data inserted.")
