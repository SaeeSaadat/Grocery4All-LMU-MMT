from database_manager import _get_connection_and_cursor


def record_command(command: str):
    with _get_connection_and_cursor(True) as (conn, cursor):
        cursor.execute("INSERT INTO command_history (command) VALUES (?)", (command,))
