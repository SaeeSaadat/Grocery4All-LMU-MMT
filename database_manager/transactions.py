import logging
from typing import List, Optional

from database_manager import _get_connection_and_cursor
from inventory.transactions import Transaction, SellTransaction, RestockTransaction, AddTransaction


def save_transaction_to_database(transaction_type: str, product_id: int, quantity: int = 0, value: float = 0.0) -> int:
    """
    This function will save the transaction to the database.
    :param transaction_type: Either `Add`, 'Sell' or 'Restock'
    :param product_id: the product that the transaction is about
    :param quantity: How many units of the product are involved in the transaction (0 for `Add`)
    :param value: How much money is involved in the transaction (0.0 for `Add`)
    :return: ID of the new transaction
    """
    with _get_connection_and_cursor(commit=True) as (_, cursor):
        cursor.execute("INSERT INTO transactions (type, product_id, quantity, total_value) VALUES (?, ?, ?, ?)",
                       (transaction_type, product_id, quantity, value))
    logging.info("Saved new %s transaction with id #%d object for product #%d to the database",
                 transaction_type, cursor.lastrowid, product_id)
    return cursor.lastrowid


def get_transactions(transaction_type: Optional[str] = None, limit: int = 10) -> List[dict]:
    """
    gets recent transactions from the database
    :param transaction_type: type of transactions required
    :param limit: number of rows to retrieve
    :return: list of dictionaries containing transactions info
    """
    query = "SELECT * FROM transactions"
    if transaction_type:
        query += f" WHERE type = '{transaction_type}'"
    query += " ORDER BY ROWID DESC"
    with _get_connection_and_cursor(return_dict=True) as (_, cursor):
        cursor.execute(query)
        return cursor.fetchmany(limit)


def get_all_product_transactions(product) -> List[Transaction]:
    """
    gets all the transactions related to the given product
    :param product: the product object of the product in question
    :return: list of transactions
    """
    with _get_connection_and_cursor(return_dict=True) as (_, cursor):
        cursor.execute("SELECT * FROM transactions WHERE product_id = ?", (product.product_id,))
        result: List[Transaction] = []
        for transaction_dict in cursor.fetchall():
            transaction_type = transaction_dict['type']
            if transaction_type == 'Add':
                result.append(AddTransaction(product))
            elif transaction_type == 'Sell':
                result.append(SellTransaction(product, transaction_dict['quantity'], transaction_dict['total_value']))
            elif transaction_type == 'Restock':
                result.append(
                    RestockTransaction(product, transaction_dict['quantity'], transaction_dict['total_value']))
            else:
                raise Exception('Invalid transaction type found in database!')

    return result


def get_product_sold_count(product_id: int) -> int:
    with _get_connection_and_cursor() as (_, cursor):
        cursor.execute('SELECT COUNT(*) FROM transactions WHERE product_id = ? AND type = ?', (product_id, 'Sell'))
        return cursor.fetchone()[0]


def get_product_sold_value(product_id: int) -> float:
    with _get_connection_and_cursor() as (_, cursor):
        cursor.execute('SELECT SUM(total_value) FROM transactions WHERE product_id = ? AND type = ?',
                       (product_id, 'Sell'))
        result = cursor.fetchone()
        return result[0]


def get_product_purchased_count(product_id: int) -> int:
    with _get_connection_and_cursor() as (_, cursor):
        cursor.execute('SELECT COUNT(*) FROM transactions WHERE product_id = ? AND type = ?', (product_id, 'Restock'))
        return cursor.fetchone()[0]


def get_product_purchased_value(product_id: int) -> float:
    with _get_connection_and_cursor() as (_, cursor):
        cursor.execute('SELECT SUM(total_value) FROM transactions WHERE product_id = ? AND type = ?',
                       (product_id, 'Restock'))
        return cursor.fetchone()[0]
