"""
Palindrome Checker Module

This module contains a function `palindrome_checker` to determine whether
a given word or phrase is a palindrome. A palindrome reads the same
forward and backward, ignoring case and spaces.
"""

from typing import Any


def palindrome_checker(word: Any) -> bool:
    """
    Check if a given word or phrase is a palindrome.

    A palindrome is a word that reads the same forward and backward,
    ignoring case and spaces.

    Args:
        word (Any): The word or phrase to check. Must be of type `str`.

    Returns:
        bool: True if the input is a palindrome, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> is_palindrome("madam")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")

    # Normalize the word by making it lowercase and removing spaces.
    cleaned_word = word.lower().replace(" ", "")

    # Check if the word is the same forward and backward.
    return cleaned_word == cleaned_word[::-1]
