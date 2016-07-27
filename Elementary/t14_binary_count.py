"""
For the Robots the decimal format is inconvenient. If they need to count to "1", their computer brains want to count it
in the binary representation of that number.
You are given a number (a positive integer). You should convert it to the binary format and count how many unities (1)
are in the number spelling. For example: 5 = 101 contains two unities, so the answer is 2.

Input: A number as a positive integer.
Output: The quantity of unities in the binary form as an integer.

Example:
checkio(4) == 1
checkio(15) == 4
checkio(1) == 1
checkio(1022) == 9

How it is used: How to convert a number to the binary form. It can be useful for Computer Science purposes.
"""


def checkio(number):
    binary = []
    while number > 0:
        remainder = number % 2
        binary.append(remainder)
        number //= 2
    binary.reverse()
    return binary.count(1)

# Examples:
print(checkio(4))
print(checkio(15))
print(checkio(1))
print(checkio(1022))
