"""
In this task, you are given a set of words in lower case. Check whether there is a pair of words, such that one word is
the end of another (a suffix of another).
For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", so the result is True.

Input: Words as a set of strings.
Output: True or False, as a boolean.

Example:

checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False
"""


def checkio(words_set):
    for word1 in words_set:
        for word2 in words_set:
            if word1 != word2 and word1.endswith(word2):
                return True
    return False

# Examples:
print(checkio({"hello", "lo", "he"}))
print(checkio({"hello", "la", "hellow", "cow"}))
print(checkio({"walk", "duckwalk"}))
print(checkio({"one"}))
print(checkio({"helicopter", "li", "he"}))
