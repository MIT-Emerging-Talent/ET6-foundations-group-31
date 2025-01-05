"""
This module provides a function for sorting the characters in a string.

The function sorts all characters in a string alphabetically.
It raises appropriate errors for invalid input types or empty strings.

@author: May Mon Thant
"""


def string_sort(input_string: str) -> str:
    """Sort the characters in the input string alphabetically.

    Args:
        input_string (str): The string whose characters are to be sorted.
                            Must be a non-empty string.

    Returns:
        str: A string containing the characters of `input_string`
             sorted alphabetically.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the string is empty.

    Examples:
        >>> string_sort("hello")
        'ehllo'
        >>> string_sort("Python")
        'Phnoty'
        >>> string_sort("12345")
        '12345'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")
    if not input_string:
        raise ValueError("Input string cannot be empty.")

    return "".join(sorted(input_string))
