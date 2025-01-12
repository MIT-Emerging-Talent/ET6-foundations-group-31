"""
Module: longest_zero_substring

Description: This module provides a function to calculate the length
of the longest substring of zeros ('0') after eliminating pairs of consecutive ones ('1').

Created on: 03-01-2025
@author: MD Jubayer Khan
"""


def longest_zero_substring(s: str) -> int:
    """
    Calculate the length of the longest substring of zeros ('0')
    after eliminating pairs of consecutive ones ('1').

    Parameters:
        s (str): The binary string to process. It is expected to contain
                only '0' and '1'.

    Returns:
        int: The length of the longest substring of zeros ('0').

    Raises:
        ValueError: If the input string contains characters other than '0' or '1'.

    Examples:
        >>> longest_zero_substring("1100100")
        2

        >>> longest_zero_substring("0001110000")
        4

        >>> longest_zero_substring("1")
        0

        >>> longest_zero_substring("0")
        1
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    if any(c not in "01" for c in s):
        raise ValueError("Input string must contain only '0' and '1'.")

    stack = []
    for c in s:
        if c == "1" and stack and stack[-1] == "1":
            stack.pop()
        else:
            stack.append(c)

    cnt = 0
    temp_cnt = 0
    while stack:
        if stack.pop() == "0":
            temp_cnt += 1
            cnt = max(cnt, temp_cnt)
        else:
            temp_cnt = 0

    return cnt
