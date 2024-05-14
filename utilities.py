"""
This module contains utility functions that are used in the project.
"""
import os
from typing import Optional


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


def get_red_string(message: str) -> str:
    return f"\033[91m{message}\033[0m"


def print_warning(message: str):
    # print in red!
    print(get_red_string(message))


def get_valid_input(input_message: str,
                    allow_empty: bool = False,
                    error_message: str = 'Please provide a valid input!',
                    validation_function: callable = None,
                    default: str = ''
                    ) -> str:
    """
    This function will take an input from the user and checks if it's valid.
    If it's not, it will repeat the input question until a valid input is provided.
    :param input_message: The message to be displayed to the user
    :param allow_empty: if true, an empty input from the user will be accepted
    :param error_message: The error message to be displayed if the input is not an integer
    :param validation_function: a function that will check the input value for additional conditions
    :param default: The default value to return if the answer is empty
    :return: the entered input as an integer (or None if input was empty)
    """
    while True:
        answer = input(input_message)

        if answer == "":
            if not allow_empty:
                print(error_message)
                continue
            else:
                return default
        try:
            if validation_function is not None and not validation_function(answer):
                print(error_message)
                continue
        except ValueError:
            print(error_message)
            continue
        return answer


def int_input(input_message: str,
              allow_empty: bool = False,
              error_message: str = 'Please provide a valid number',
              validation_function: callable = None,
              default: Optional[int] = None
              ) -> Optional[int]:
    """
    This function will take an integer input from the user.
    If the provided input is not an integer, the question will be repeated unless a keyboard interrupt happens!
    :param input_message: The message to be displayed to the user
    :param allow_empty: if true, an empty input from the user will be accepted
    :param error_message: The error message to be displayed if the input is not an integer
    :param validation_function: a function that will check the input value for additional conditions
    :param default: The default value to return if the answer is empty
    :return: the entered input as an integer (or None if input was empty)
    """
    res = get_valid_input(input_message,
                          allow_empty,
                          error_message,
                          validation_function=lambda x: validation_function(int(x))
                          )
    return int(res) if res else default


def float_input(input_message: str,
                allow_empty: bool = False,
                error_message: str = 'Please provide a valid number',
                validation_function: callable = None,
                default: Optional[float] = None
                ) -> Optional[float]:
    """
    Same as int_input, but for floats!
    """
    res = get_valid_input(input_message,
                          allow_empty,
                          error_message,
                          validation_function=lambda x: validation_function(float(x))
                          )

    return float(res) if res else default
