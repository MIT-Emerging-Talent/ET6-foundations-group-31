"""
Module: word_comparator

Description: This module provides a function to compare two words
by checking if their sorted characters are the same.

Created on: 03 01 25
@author: MD Jubayer Khan
"""


def word_comparator(word1: str, word2: str) -> bool:
    """
    Compares two words by sorting their characters and checking for equality.

    Parameters:
        word1 (str): The first word to compare.
        word2 (str): The second word to compare.

    Returns:
        bool: True if the sorted characters of both words are the same, False otherwise.

    Raises:
        TypeError: If either input is not a string.
    """
    if not isinstance(word1, str):
        raise TypeError("The first input must be a string.")
    if not isinstance(word2, str):
        raise TypeError("The second input must be a string.")
    return sorted(word1) == sorted(word2)
