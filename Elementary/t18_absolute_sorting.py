"""
The array (a tuple) given as input has various numbers. You should sort it, but sort it by absolute value in ascending order.
For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20).
Your function should return the sorted list or tuple.

Input: An array of numbers, a tuple.
Output: The list or tuple (but not a generator) sorted by absolute values in ascending order.

Example:
checkio((-20, -5, 10, 15)) == [-5, 10, 15, -20] # or (-5, 10, 15, -20)
checkio((1, 2, 3, 0)) == [0, 1, 2, 3]
checkio((-1, -2, -3, 0)) == [0, -1, -2, -3]

"""


def checkio(numbers):
    return sorted(numbers, key=abs)

# Examples:
print(checkio((-20, -5, 10, 15)))
print(checkio((1, 2, 3, 0)))
print(checkio((-1, -2, -3, 0)))
