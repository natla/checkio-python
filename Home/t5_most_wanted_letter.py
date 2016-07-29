"""
You are given a text, which contains different english letters and punctuation symbols.
You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet.
For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.
Output: The most frequent letter in lower case as a string.

Example:
checkio("Hello World!") == "l"
checkio("How do you do?") == "o"
checkio("One") == "e"
checkio("Oops!") == "o"
checkio("AAaooo!!!!") == "a"
checkio("abe") == "a"

How it is used: For most decryption tasks you need to know the frequency of occurrence for various letters
in a section of text. For example: we can easily crack a simple addition or substitution cipher if we know
the frequency in which letters appear. This is interesting stuff for language experts!
"""
import string

letters = string.ascii_lowercase


def checkio(text):
    found = []
    for symbol in text.lower():
        if symbol in letters:
            found.append(symbol)

    found.sort()
    if len(found) <= 1:
        return "".join(found)
    else:
        max_count = 0
        for i in range(len(found) - 1):
            count = max(found.count(found[i]), found.count(found[i + 1]))
            if max_count < count:
                max_count = count

    return [f for f in found if found.count(f) == max_count][0]


# Examples:
print(checkio("Hello World!"))
print(checkio("How do you do?"))
print(checkio("One"))
print(checkio("Oops!"))
print(checkio("AAaooo!!!!"))
print(checkio("abe"))
print(checkio("Z"))
print(checkio(""))
