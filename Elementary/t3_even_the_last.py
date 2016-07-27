"""
You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...)
then multiply this summed number and the final element of the array together.
Don't forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.

Example:
checkio([0, 1, 2, 3, 4, 5]) == 30
checkio([1, 3, 5]) == 30
checkio([6]) == 36
checkio([]) == 0
"""


def checkio(array):
    if len(array) == 0:
        return 0
    else:
        return sum(array[::2]) * array[-1]

# Examples:
print(checkio([0, 1, 2, 3, 4, 5]))
print(checkio([1, 3, 5]))
print(checkio([6]))
print(checkio([]))
