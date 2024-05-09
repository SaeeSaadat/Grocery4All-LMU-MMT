"""
This module is in charge of handling the database operations.
No other module should have direct access to the database.
This way, we can easily change the database implementation without affecting the rest of the code.
"""
import os
import sqlite3
import logging
from contextlib import contextmanager


@contextmanager
def _get_connection_and_cursor(commit: bool = False):
    """
    This function is used to get the connection and cursor objects.
    This method is private and must not be accessed by outside modules.
    :return: connection and cursor objects
    """
    conn = sqlite3.connect('database_manager/database.db')
    try:
        cursor = conn.cursor()
        yield conn, cursor
    finally:
        if commit:
            conn.commit()
        conn.close()


def initialize_database():
    """
    This function is used to initialize the database, if and only if the database file doesn't already exist.
    """

    # Check if database file exists
    if os.path.exists('database_manager/database.db'):
        raise Exception("Database already exists.")

    # Create the database file
    open('database_manager/database.db', 'w').close()

    with _get_connection_and_cursor(True) as (conn, cursor):
        # run the initialize_database.sql script
        with open('database_manager/initialize_database.sql', 'r') as sql_script:
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
        with open('database_manager/mock_data.sql', 'r') as sql_script:
            cursor.executescript(sql_script.read())
    logging.info("Mock data inserted.")
