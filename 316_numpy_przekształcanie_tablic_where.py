#Zadanie 6. Masz podaną tablicę o rozmiarze 2x3 składającą się z elementów:

#5 10 15

#6 70 20
#Za pomocą odpowiedniej funkcji, przekształć tą tablicę w następujący sposób:
#Liczby, które są większe równe od 15 zamień, na liczby równe 100
#Liczby, które są mniejsze od 15, zamień na zera. Wyświetl tablicę wynikową.

import numpy as np

my_tab = np.array([[5, 10, 15], [6, 10, 70]])

print(my_tab)

a = np.where(my_tab >= 15, 100, 0)
print(a)
