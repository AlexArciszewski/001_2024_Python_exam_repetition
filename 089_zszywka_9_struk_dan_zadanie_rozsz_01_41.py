# Zad 1.
# Utwórz dwie listy a i b. Sprawdź czy listy te mają chociaż jeden wspólny element.

a = [1, "a", True]
b = [9, "b", True]

for el_a in a:
    if el_a in b:
        print(f'There is atleast one shared element wich is: {el_a}')


