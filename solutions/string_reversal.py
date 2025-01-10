"""
Module: string_reversal
This module contains a function to reverse the characters of a given string.

@author: Safa Saber
"""


def string_reversal(input_string: str) -> str:
    """
    Reverse the characters of the given string.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        ValueError: If the input is not a string.

    Doctests:
        >>> string_reversal("hello")
        'olleh'
        >>> string_reversal("world")
        'dlrow'
        >>> string_reversal("Safa")
        'afaS'
        >>> string_reversal("Python")
        'nohtyP'
    """
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")

    return input_string[::-1]
