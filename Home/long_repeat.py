"""
Here you should find the length of the longest substring that consists of the same letter.
For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa".
The last substring is the longest one which makes it an answer.

Input: String.

Output: Int.
"""


def long_repeat(line):
    """
       Return the length of the longest substring that consists of the same char
    """
    substring_list = []
    if len(line) is 0:
        return 0
    for idx in range(len(line) - 1):
        length = 1
        while line[idx] == line[idx + 1]:
            if idx + 1 == len(line) - 1:
                length += 1
                break
            length += 1
            idx += 1
        substring_list.append(length)
    return max(substring_list)


if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4
    assert long_repeat('ddvvrwwwrgggg') == 4
    assert long_repeat('abababaab') == 2
    assert long_repeat('') == 0
