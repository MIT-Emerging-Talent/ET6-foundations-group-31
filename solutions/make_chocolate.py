"""
This module provides a function for determining the number of small chocolate bars needed
to meet a specific goal weight, prioritizing the use of big bars.

The function calculates the required small bars after using as many big bars as possible,
ensuring the goal is achievable. It raises appropriate errors for invalid inputs.

@author: May Mon Thant
"""


def make_chocolate(small: int, big: int, goal: int) -> int:
    """
    Determine the number of small bars needed to meet the goal weight.

    Args:
        small (int): The number of small bars available (1 kg each). Must be non-negative.
        big (int): The number of big bars available (5 kg each). Must be non-negative.
        goal (int): The target weight of the chocolate package. Must be non-negative.

    Returns:
        int: The number of small bars needed to meet the goal.
             Returns -1 if the goal cannot be achieved.

    Raises:
        ValueError: If any of the inputs are negative.

    Examples:
        >>> make_chocolate(4, 1, 9)
        4
        >>> make_chocolate(4, 1, 10)
        -1
        >>> make_chocolate(4, 1, 7)
        2
    """
    if small < 0 or big < 0 or goal < 0:
        raise ValueError("All inputs must be non-negative integers.")

    # Use as many big bars as possible without exceeding the goal
    max_big_bars = goal // 5
    big_bars_used = min(max_big_bars, big)

    # Calculate the remaining weight to be covered with small bars
    remaining_goal = goal - big_bars_used * 5

    # Check if the remaining goal can be achieved with small bars
    if remaining_goal <= small:
        return remaining_goal
    else:
        return -1
