"""
The function should recognise if a subject line is stressful.
A stressful subject line means that all letters are in uppercase, and/or ends by at least 3 exclamation marks,
and/or contains at least one of the following “red” words: "help", "asap", "urgent".
Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
even in a very loooong way "HHHEEEEEEEEELLP"

Input: Subject line as a string.

Output: Boolean.

Precondition: Subject can be up to 100 letters
"""


def is_stressful(subj):
    """
        Recognise stressful subject.
    """

    # A list of stressful words
    stressful_list = ["help", "asap", "urgent"]

    def strip_punctuation(string):
        """
        Strip the punctuation from the string through a list comprehension.
        :arg string - the word to strip any punctuation from
        :return str - the word without punctuation
        """
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        return "".join(s for s in string if s not in punctuation)

    def shorten_long_word(string):
        """
        Iterate through each of the words in the stressful list
        and if a letter is found in the string provided as an arg,
        concatenate the found letters in a new word.
        :arg string - the long word to shorten
        :return str - the new (shortened) word if it is in the stressful list
        or the original string if none of the new words is found in the list
        """
        for word in stressful_list:
            new_word = "".join(letter for letter in word if letter in string.lower())
            if new_word in stressful_list:
                return new_word
        return string

    if subj == subj.upper():
        return True
    if subj.endswith("!!!"):
        return True
    for word in subj.split():
        word = strip_punctuation(word)
        if len(word) > 4:
            word = shorten_long_word(word)
        if word.lower() in stressful_list:
            return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False
    assert is_stressful("I neeed HELP") == True
    assert is_stressful("aasap") == True
    assert is_stressful("UUUURGGGEEEEENT here") == True
    print('Done! Go Check it!')