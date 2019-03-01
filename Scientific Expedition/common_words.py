"""
You are given two string with words separated by commas. Try to find what is common between these strings.
The words are not repeated in the same string.

Your function should find all of the words that appear in both strings.
The result must be represented as a string of words separated by commas in alphabetic order.

Input: Two arguments as strings.
Output: The common words as a string.

Example:
checkio("hello,world", "hello,earth") == "hello"
checkio("one,two,three", "four,five,six") == ""
checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

How it is used: Here you can learn how to work with strings and sets.
This knowledge can be useful for linguistic analysis.
"""


# solution using list comprehension:
def checkio(first, second):
    return ",".join([w for w in sorted(first.split(",")) if (first.split(",") + second.split(",")).count(w) > 1])


# Examples:
print(checkio("hello,world", "hello,earth"))
print(checkio("one,two,three", "four,five,six"))
print(checkio("one,two,three", "four,five,one,two,six,three"))