"""Module: cat_dog
This module contains a function to check if the number of occurrences
of the substrings "cat" and "dog" are the same in a given string.
@author: May Mon Thant
"""


def cat_dog(input_string: str) -> bool:
    """
    Check if the string "cat" and "dog" appear the same number of times
    in the given string.

    Args:
        input_string (str): The input string to be checked.
            Maximum allowed length is 15 characters.

    Returns:
        bool: True if "cat" and "dog" appear the same number of times,
            otherwise False.

    Raises:
        TypeError: If the input is not a string.
        AssertionError: If the input string length exceeds 15 characters.

    Doctests:
        >>> cat_dog("catdog")
        True
        >>> cat_dog("catcat")
        False
        >>> cat_dog("1cat1cadodog")
        True
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    max_length = 15  # Define a reasonable length limit for the input string
    assert (
        len(input_string) <= max_length
    ), f"Input string is too long. Maximum allowed length is {max_length} characters."

    return input_string.count("cat") == input_string.count("dog")
