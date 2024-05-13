import logging

from database_manager import _get_connection_and_cursor


def save_transaction_to_database(transaction_type: str, product_id: int, quantity: int = 0, value: float = 0.0):
    """
    This function will save the transaction to the database.
    :param transaction_type: Either `Add`, 'Sale' or 'Restock'
    :param product: the product that the transaction is about
    :param quantity: How many units of the product are involved in the transaction (0 for `Add`)
    :param value: How much money is involved in the transaction (0.0 for `Add`)
    """
    with _get_connection_and_cursor(commit=True) as (conn, cursor):
        cursor.execute("INSERT INTO transactions (type, product_id, quantity, total_price) VALUES (?, ?, ?, ?)",
                       (transaction_type, product_id, quantity, value))
    logging.info("Saved new transaction with id #%d object for product #%d to the database", cursor.lastrowid,
                 product_id)
