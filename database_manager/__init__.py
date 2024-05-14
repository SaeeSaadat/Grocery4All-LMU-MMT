"""
This module is in charge of handling the database operations.
No other module should have direct access to the database.
This way, we can easily change the database implementation without affecting the rest of the code.
"""
import os
import shutil
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

    DB_FILE_NAME = db_name if db_name.startswith('database_manager') else f'database_manager/{db_name}'
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


def backup_database():
    """
    This function is used to backup the current database.
    It will create a copy of the current database file.
    :return:
    """
    # copy the current database file to a backup file
    shutil.copyfile(DB_FILE_NAME, f'{DB_FILE_NAME}.backup')
    logging.info(f"Database backup created. -> {DB_FILE_NAME}.backup")
    print(f"Database backup created successfully in {DB_FILE_NAME}.backup!")


def reset_database():
    # rename the current database file to backup
    os.rename(DB_FILE_NAME, f'{DB_FILE_NAME}.backup')
    logging.info(f"Database backup created. -> {DB_FILE_NAME}.backup")
    print(f"Database backup created. -> {DB_FILE_NAME}.backup")
    initialize_database(DB_FILE_NAME)
    logging.warning("Database reset.")
    print("Database reset successfully!")
    print("You may restore the previous data using the 'restore' command.\n")


def restore_database():
    """
    This function is used to restore the database from the backup.
    It will swap the current database with the backup.
    If there's no backup, it will raise an exception.
    :return:
    """
    os.rename(DB_FILE_NAME, f'{DB_FILE_NAME}.backup.temp')
    os.rename(f'{DB_FILE_NAME}.backup', DB_FILE_NAME)
    os.rename(f'{DB_FILE_NAME}.backup.temp', f'{DB_FILE_NAME}.backup')
    logging.info("Database restored from backup.")
    print("Database restored successfully!")
    print("You may restore the previous data using the 'restore' command.")
