# Pytanie 18 - napisz funkcję, która będzie pobierać dwie liczby
# i sprawdzać czy pierwsza z nich jest podzielna przez drugą


import pytest


def checking_func(first_number: int, second_number: int) -> bool:
    """ Function to check if the first numer can be divided by second numer. """
    if first_number % second_number == 0:
        return True
    else:
        return False


print(checking_func(14, 7))
print(checking_func(5, 10))


@pytest.mark.parametrize("first_number, second_number",[(14, 7), (10, 5), (8, 4)])
def test_checking_func(first_number: int, second_number: int) -> None:
    """ Parametrize  test for test checking function"""
    assert checking_func(first_number, second_number) == True


@pytest.mark.parametrize("first_number, second_number",[(15, 7), (11, 5), (9, 4)])
def test_is_not_checking_func(first_number: int, second_number: int) -> None:
    """ Parametrize  test for test checking function"""
    assert checking_func(first_number, second_number) == False






