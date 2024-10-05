def is_palindrome3(word: str) -> bool:
    """Function that checks if a word is a palindrome"""
    start = 0
    end = len(word) - 1
    while start <= end:
        if word[start] != word[end]:
            return False
        else:
            start += 1
            end -= 1

    return True


print(is_palindrome3('radar'))


def is_palindrome2(word: str) -> bool:
    """Function to check if a word writen as a string is a palindrome. Returns boolean True/False """
    word_lower = word.lower()
    if word_lower == word_lower[::-1]:
        return True
    else:
        return False


print(is_palindrome2('radar'))


def is_palindrome5(word: str) -> bool:
    return True if word == word[::-1] else False


print(is_palindrome5('radar'))