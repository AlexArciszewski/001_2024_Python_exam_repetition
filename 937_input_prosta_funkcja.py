# Pytanie 18 - napisz funkcję, która będzie pobierać dwie liczby
# i sprawdzać czy pierwsza z nich jest podzielna przez drugą


def checking_func(first_number: int, second_number: int) -> bool:
    """ Function to check if  the first numer can be divided by second numer. """
    if first_number % second_number == 0:
        return True
    else:
        return False


print(checking_func(5, 10))


