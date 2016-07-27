"""
You are given a string with words and numbers separated by whitespaces (one space).
The words contain only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.

Example:
checkio("Hello World hello") == True
checkio("He is 123 man") == False
checkio("1 2 3 4") == False
checkio("bla bla bla bla") == True
checkio("Hi") == False
"""


def checkio(words):
    words = words.split()
    total = 0
    for word in words:
        if word.isalpha():
            total += 1
            if total == 3:
                break
        else:
            total = 0
    return total == 3

# Examples:
print(checkio("Hello World hello"))
print(checkio("He is 123 man"))
print(checkio("1 2 3 4"))
print(checkio("bla bla bla bla"))
print(checkio("Hi"))
