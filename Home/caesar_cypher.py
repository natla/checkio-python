"""
Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.)
using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance.
For example ("a b c", 3) == "d e f"

Input: A secret message as a string (lowercase letters only and white spaces)

Output: The same string, but encrypted
"""


def to_encrypt(text, delta):
    """
       Encrypt the text translating the letters it uses by the delta argument
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encryption_alphabet = alphabet[delta:] + alphabet[:delta]
    return text.translate(text.maketrans(alphabet, encryption_alphabet))

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")