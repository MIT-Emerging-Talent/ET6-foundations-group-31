def mean_and_median(values):
    """
    Functions:
      Get the mean and median of a sorted list of `values`

    Args:
      values (iterable of float): A list of numbers

    Returns:
      tuple (float, float): The mean and median

    Raises:
          TypeError: If `values` is not a list.
          
    @author: Myat Charm
    Created on Dec 27, 2024.
    """
    if not isinstance(values, list):
        raise TypeError("Input must be a list.")
    if len(values) == 0:
        return None, None
    mean = sum(values) / len(values)
    values = sorted(values)
    midpoint = int(len(values) / 2)
    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]

    return mean, median
