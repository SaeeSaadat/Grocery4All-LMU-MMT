import os


def print_message(text_file: str):
    with open(text_file, 'r') as f:
        message = f.read()
    try:
        print(message.center(os.get_terminal_size().columns))
    except OSError:
        # In some terminal windows (like in the IDE) might happen, because of the .get_terminal_size() function
        print(message)


def clear_terminal():
    """
    Clear terminal command for different platforms
    """
    command = "clear"  # Linux and macOS
    if os.name == "nt":  # Windows
        command = "cls"
    os.system(command)