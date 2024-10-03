# Zad 1.
# Utwórz dwie listy a i b. Sprawdź czy listy te mają chociaż jeden wspólny element.

a = [1, "a", True]
b = [9, "b", True]

for el_a in a:
    if el_a in b:
        print(f'There is atleast one shared element wich is: {el_a}')
    else:
        print("none")

# Opcja lepsza wykorzystac zaleznosci zbiorów

# Tworzenie dwóch list
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

# Sprawdzenie, czy listy mają wspólny element
if set(a) & set(b):
    print("Listy mają wspólny element.")
else:
    print("Listy nie mają wspólnego elementu.")

# set(a) & set(b) zwraca przecięcie tych dwóch zbiorów, czyli wspólne elementy.