"""
fixed_password_checker

Description: This module provides a function to validate a single password attempt.
The function checks the provided password against a fixed correct password and returns
whether it is "Correct" or "Wrong".

Created on: 03 01 25
@author: MD Jubayer Khan
"""


def password_checker(attempt: int, correct_password: int = 1999) -> str:
    """
    Validates a single password attempt against the fixed correct password.

    Parameters:
        attempt (int): The password attempt.
        correct_password (int): The fixed password to validate against (default: 1999).

    Returns:
        str: "Correct" if the attempt matches the fixed password, "Wrong" otherwise.

    Examples:
        >>> validate_password(1234)
        'Wrong'

        >>> validate_password(1999)
        'Correct'
    """
    return "Correct" if attempt == correct_password else "Wrong"
