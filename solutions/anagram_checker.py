"""
Anagram Checker

This module contains a function to check if two strings are anagrams of each other.
Two strings are considered anagrams if they have the same characters with the same frequency,
ignoring spaces and case sensitivity.

"""


def anagram_checker(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Raises:
        TypeError: If either argument is not a string.

    Examples:
        >>> anagram_checker("listen", "silent")
        True
        >>> anagram_checker("triangle", "integral")
        True
        >>> anagram_checker("hello", "world")
        False
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")

    # Normalize by removing spaces and converting to lowercase
    normalized_str1 = str1.replace(" ", "").lower()
    normalized_str2 = str2.replace(" ", "").lower()

    # Check if sorted characters match
    return sorted(normalized_str1) == sorted(normalized_str2)
