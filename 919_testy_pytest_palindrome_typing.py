# Palindromy ->'bob','kajak','anna', 'sedes', '22022022'
import pytest
from typing import List


def is_palindrome(word: str) -> bool:
    """Function to check if a word is a palindrome.Return"""
    return word == word[::-1]


print(is_palindrome('kajak'))


def test_is_palindrome() -> None:
    """Test if a word is a palindrome."""
    assert is_palindrome('bob') == True
    assert is_palindrome('kajak') == True
    assert is_palindrome('anna') == True
    assert is_palindrome('sedes') == True
    assert is_palindrome('22022022') == True


def test_is_not_palindrome() -> None:
    """Test if a word is not a palindrome."""

    assert is_palindrome('test') == False
    assert is_palindrome('palindrom') == False
    assert is_palindrome('warszawa') == False


# pytest.mark.parametrize

@pytest.mark.parametrize('word', ['bob', 'kajak', 'anna', 'sedes', '22022022'])  # word i pozostałe do testów
def test_is_palindrome_with_parametrize(word: str) -> None:
    """Parametrize test if a word is a palindrome."""
    assert is_palindrome(word)
    # dla każdego ze słów w liscie osobny test jest wykonywany wiec wystarczy jeden assert  mamy 5 testow


@pytest.mark.parametrize('word', ['test', 'palindrom', 'warszawa'])
def test_is_not_palindrome_with_parametrize(word: str) -> None:
    """ Test if a word is not a palindrome."""
    assert is_palindrome(word) == False