#  Dictionary comprehension
#
# Używany do tworzenia nowych słowników, bazując na istniejących danych.
# Przykłady:


#Tworzenie słownika, gdzie klucz to liczba, a wartość to jej kwadrat:

squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# Odwrócenie kluczy i wartości w słowniku:

original_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in original_dict.items()}
print(reversed_dict)
# {1: 'a', 2: 'b', 3: 'c'}