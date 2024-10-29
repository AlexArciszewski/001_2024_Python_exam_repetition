# Pytanie 42 - przy użyciu wyszukiwania binarnego sprawdź
# czy liczba 341 znajduje się w posortowanej liście num_list

num_list = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]


def binary_search(requested_num: int) -> str:
    """Function used for binary search"""
    left_position = 0
    right_position = len(num_list) - 1
    while left_position <= right_position:
        middle_position = (left_position + right_position) // 2
        if num_list[middle_position] == requested_num:
            print(f"{requested_num} is on the list")
            break
        elif middle_position < requested_num:
            left_position = middle_position + 1
        else:
            right_position = middle_position - 1
    else:
        print(f"{requested_num} is not on that list")

binary_search(68)





P= [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]


szukana = 100        # zmienna przechowująca szukaną wartość
lewy = 0             # indeks lewy określający początek przeszukiwanego zakresu listy
prawy = len(P) - 1   # indeks prawy określający koniec przeszukiwanego zakresu listy
while lewy <= prawy: # dopóki indeks lewy jest mniejszy lub równy prawemu
    srodkowy = (lewy + prawy) // 2  # wyliczamy indeks srodkowy, jako średnią indeksów lewy i prawy (// - zwraca część całkowitą z dzielenia)
    if P[srodkowy] == szukana:  # jeśli lista od inseksu srodkowy zawiera szukaną wartość
        print(f"Liczba {szukana} znajduje się na liście.") # wypisz informację, że wartość znaleziono
        break        # i przerwij działanie pętli while
    elif P[srodkowy] < szukana:  # jeśli lista od indeksu srodkowy zawiera wartość mniejszą niż szukana
        lewy = srodkowy + 1      # przesuń indeks lewy na pozycję o jeden większą niz srodkowy
    else:                        # w przeciwnym wypadku (czyli jeśli lista od indeku srodkowy zawiera wartość większa niż szukana)
        prawy = srodkowy - 1     # przesuń indeks prawy na pozycję o jeden mniejszą niż srodkowy jeśli liczba jest większa
else:                 # jeśli pętla while skończy się wykonywać, bo warunek w niej zawarty zwróci False, to wtedy uruchomi się ten else
    print(f"Liczby {szukana} nie ma na liście.")