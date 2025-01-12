from typing import List, Tuple


def mean_and_median(values: List[float]) -> Tuple[float, float]:
    """
    Calculate the mean and median of a list of numbers.

    Args:
        values (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: The mean and median of the list.

    Raises:
        TypeError: If `values` is not a list or contains non-float elements.
        ValueError: If `values` is an empty list.

    Strategy:
        - Validate the input type and elements.
        - Calculate the mean by summing the values and dividing by the number of elements.
        - Sort the list and calculate the median based on the number of elements.
    """
    if not isinstance(values, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, (int, float)) for x in values):
        raise TypeError("All elements in the list must be integers or floats.")
    if len(values) == 0:
        raise ValueError("Input list must not be empty.")

    mean = sum(values) / len(values)
    values = sorted(values)
    midpoint = len(values) // 2
    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]

    return mean, median
