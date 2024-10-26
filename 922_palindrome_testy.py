# Pytanie 12 - napisz funkcję sprawdzającą czy podane słowo jest palindromem.
# Uruchom funkcję aby sprawdzić czy palindromami są słowa "kajak" i "anakonda".

# Anna # gawron # radar

# Dodajemy testy

import pytest


def is_palindrome(word: str) -> bool:
    """Function to check if a word writen as a string is a palindrome. Returns boolean True/False """
    if word == word[::-1]:
        return True
    else:
        return False


print(is_palindrome('radar'))
print(is_palindrome('Anna'))
print(is_palindrome('gawron'))

assert is_palindrome('radar') == True
assert is_palindrome('Anna') == False
assert is_palindrome('gawron') == False


@pytest.mark.parametrize("word", ["radar", "Anna", "gawron"])
def test_is_palindrome(word):
    """Parametrize test if a word is a palindrome."""
    # assert is_palindrome(word) == True
    assert is_palindrome('radar') == True
    assert is_palindrome('Anna') == False
    assert is_palindrome('gawron') == False




# Opcja B palindrom pomijajacy duze litery


def is_palindrome2(word: str) -> bool:
    """Function to check if a word writen as a string is a palindrome. Returns boolean True/False """
    word_lower = word.lower()
    if word_lower == word_lower[::-1]:
        return True
    else:
        return False


print(is_palindrome2('radar'))
print(is_palindrome2('Anna'))

# print(is_palindrome2('gawron'))
# z testu ponizej wyrzucamy gawron i teraz załosc ma być true i tet przechodzi


@pytest.mark.parametrize("word", ["radar", "Anna"])
def test_is_palindrome2(word):
    """ Test if a word is not a palindrome."""
    assert is_palindrome2(word) == True



def is_palindrome3(word: str) -> bool:
    """Function to check if a word writen as a string is a palindrome. Returns boolean True/False """
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


def is_palindrome5(word: str) -> bool:
    """Function to check if a word writen as a string is a palindrome. Returns boolean True/False """
    return True if word == word[::-1] else False


print(is_palindrome5('radar'))

