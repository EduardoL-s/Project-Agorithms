def is_palindrome_iterative(word):
    if (len(word) == 0):
        return False
    invertWord = reversed(word)
    newWord = "".join(invertWord)

    if (word == newWord):
        return True
    return False
