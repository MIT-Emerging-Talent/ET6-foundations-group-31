from typing import List, Tuple


def mean_and_median(values: List[float]) -> Tuple[float, float]:
    """
    Functions:
      Get the mean and median of a sorted list of `values`

    Args:
      values (List[float]): A list of numbers

    Returns:
      Tuple[float, float]: The mean and median

    Raises:
      TypeError: If `values` is not a list.
    """
    if not isinstance(values, list):
        raise TypeError("Input must be a list.")
    if len(values) == 0:
        raise ValueError("Input list must not be empty.")

    mean = sum(values) / len(values)
    values = sorted(values)
    midpoint = int(len(values) / 2)
    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]

    return mean, median
