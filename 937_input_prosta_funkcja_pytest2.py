# Pytanie 18 - napisz funkcję, która będzie pobierać dwie liczby
# i sprawdzać czy pierwsza z nich jest podzielna przez drugą


import pytest


def checking_func(first_number: int, second_number: int) -> bool:
    """ Function to check if the first numer can be divided by second numer. """
    return first_number % second_number == 0


print(checking_func(14, 7))
print(checking_func(5, 10))


@pytest.mark.parametrize("first_number, second_number, expected", [(14, 7, True),  (10, 5, True),  (9, 4, False)])
def test_checking_func(first_number: int, second_number: int, expected: bool) -> None:
    """ Test that checks both True and False cases """

    assert checking_func(first_number, second_number) == expected






