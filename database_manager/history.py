from typing import List
from database_manager import _get_connection_and_cursor


def record_command(command: str):
    with _get_connection_and_cursor(True) as (conn, cursor):
        cursor.execute("INSERT INTO command_history (command) VALUES (?)", (command,))


def get_history(limit: int = 10, include_timestamp: bool = False) -> List[str]:
    with _get_connection_and_cursor(return_dict=True) as (conn, cursor):
        cursor.execute("SELECT * FROM command_history ORDER BY ROWID DESC LIMIT ?", (limit, ))
        if include_timestamp:
            return cursor.fetchall()
        return [x[0] for x in cursor.fetchall()]
