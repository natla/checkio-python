"""
Write a function that finds the longest palindromic substring of a given string. Try to be as efficient as possible!

If you find more than one substring you should return the one which is closer to the beginning.

Input: A text as a string.
Output: The longest palindromic substring.
"""


def divide_text(text):  # a helper function that's dividing the text in halves
    middle_ind = len(text) // 2
    if len(text) % 2 == 0:
        text1 = text[:middle_ind]
        text2 = text[:middle_ind - 1:-1]
    else:
        text1 = text[:middle_ind + 1]
        text2 = text[:middle_ind - 1:-1]
    return text1, text2


def longest_palindromic(text):
    original = text
    text_copy1 = text
    text_copy2 = text
    palindromes = []

    while len(text) > 0:
        text1, text2 = divide_text(text)
        if text1 == text2:
            palindromes.append(text)
            break
        else:
            text = text[:-1]  # each iteration we are removing the last letter

    while len(text_copy1) > 0:
        text1, text2 = divide_text(text_copy1)
        if text1 == text2:
            palindromes.append(text_copy1)
            break
        else:
            text_copy1 = text_copy1[1:]  # each iteration we are removing the first letter

    while len(text_copy2) > 0:
        text1, text2 = divide_text(text_copy2)
        if text1 == text2:
            palindromes.append(text_copy2)
            break
        else:
            text_copy2 = text_copy2[1:-1]  # each iteration we are removing both the first and the last letter

    try:
        return max(palindromes, key=len)
    except:
        return original[0]

# Examples:
print(longest_palindromic("artrartrt"))
print(longest_palindromic("abacada"))
print(longest_palindromic("aaaa"))
print(longest_palindromic("abc"))
print(longest_palindromic("so sad das-li"))
