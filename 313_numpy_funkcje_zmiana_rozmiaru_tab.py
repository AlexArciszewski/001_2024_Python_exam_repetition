#Zadanie 2. Stwórz tablicę składającą się z liczb od 1 do 10, po czym zmień jej rozmiar na rozmiar 2x5.
import numpy as np

my_tab = np.arange(1, 11)
print(my_tab)
#[1 2 3 4 5 6 7 8 9]

my_tab_reshaped = my_tab.reshape(2,5)
print(my_tab_reshaped)

#[[ 1  2  3  4  5]
# [ 6  7  8  9 10]]