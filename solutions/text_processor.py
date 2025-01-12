"""
text_processor

Description: This module provides functions to process texts and convert them in different ways, including counting vowels, reversing text, and converting to uppercase.

Created on: 04/01/2025
# spell-checker: disable
@author: Thilakan Jegatheeswaran
# spell-checker: enable
"""


def count_vowels(text: str) -> int:
    """
    Counts the number of vowels (a, e, i, o, u) in the given text.

    Parameters:
        text (str): The string to analyze.

    Returns:
        int: The number of vowels in the text.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> count_vowels("hello")
        2

        >>> count_vowels("world")
        1
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def reverse_text(text: str) -> str:
    """
    Reverses the given text.

    Parameters:
        text (str): The string to reverse.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> reverse_text("hello")
        'olleh'

        >>> reverse_text("world")
        'dlrow'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return text[::-1]


def to_uppercase(text: str) -> str:
    """
    Converts the given text to uppercase.

    Parameters:
        text (str): The string to convert.

    Returns:
        str: The text in uppercase.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> to_uppercase("hello")
        'HELLO'

        >>> to_uppercase("world")
        'WORLD'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return text.upper()
