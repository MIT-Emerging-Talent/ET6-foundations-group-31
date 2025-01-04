def sum_of_numbers(numbers):
  """
  Calculate the sum of all numbers in the given list.

  Args:
    numbers (list of int or float): A list containing numerical values (integers or floats).
  
  Returns:
    int or float: The sum of all the numbers in the list. The return type will match the type of the numbers in the list (int if all numbers are integers, or float if any number is a float).
  
  Example:
    >>> sum_of_numbers([1, 2, 3, 4, 5])
    15

    >>> sum_of_numbers([-1, 0, 5, -2])
    2

    >>> sum_of_numbers([10, 20, 30])
    60
  """
  total = 0  # Initialize a variable to store the sum
  for num in numbers:  # Loop through each number in the list
    total += num  # Add the current number to the total
  return total  # Return the final sum

ans = sum_of_numbers([1, 2, 3, 4, 5])  
print(ans) # Output: 15
