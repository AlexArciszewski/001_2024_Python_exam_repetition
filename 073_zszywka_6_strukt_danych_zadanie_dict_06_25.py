# Zad 6.
# Wyszukaj w zewnętrznych źródłach, jakie obiekty nie mogą być kluczami w słowniku.

# W Pythonie kluczem w słowniku może być dowolny niemodyfikowalny (immutable) typ danych.
# Oto kilka przykładów typów, które mogą służyć jako klucze:

# Liczby całkowite (integers):
# my_dict = {1: 'jeden', 2: 'dwa', 3: 'trzy'}
#
# Liczby zmiennoprzecinkowe (floats):
# my_dict = {0.1: 'zero-jeden', 0.5: 'zero-pięć', 1.2: 'jeden-dwa'}
#
# Napisy (strings):
# my_dict = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie'}
#
# Tuple (krotki), jeśli zawierają tylko niemodyfikowalne elementy:
# my_dict = {(1, 2): 'jeden-dwa', (3, 4): 'trzy-cztery'}
#
# Boolowskie wartości:
# my_dict = {True: 'prawda', False: 'fałsz'}
#
# None:
# my_dict = {None: 'brak'}

# Niemodyfikowalność klucza jest ważna, ponieważ słowniki są strukturami danych opartymi na haszowaniu,
# a klucze są używane do obliczania funkcji haszującej. Jeśli klucz jest modyfikowalny (na przykład lista),
# to nie można go używać jako klucza w słowniku, ponieważ może się zmieniać, co prowadziłoby do problemów z
# funkcją haszującą.
# Dobre praktyki obejmują stosowanie kluczy, które są czytelne i łatwe do zrozumienia, a także unikanie
# modyfikowalnych obiektów jako kluczy, chyba że są one konwertowane na niemodyfikowalne (np. tuple).