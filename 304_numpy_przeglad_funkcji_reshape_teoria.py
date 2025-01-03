
import numpy as np


#Reshape zmiana rozmiaru tablicy wielowymairowej
#przyjmuje 2 argumenty liczba wierszy i liczba kolumn  definiujace docelowy rozmiar tabeli
#podany rozmiar tablicy docelowej musi byc ozliwy do wykoannia z 2x6 da się zrobić 3x4 ale 3x5 już nie
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(c)

#[[ 1  2  3  4]
# [ 5  6  7  8]
#[ 9 10 11 12]]

d = c.reshape(2, 6)
print(d)

#[[ 1  2  3  4  5  6]
#[ 7  8  9 10 11 12]]



d = np.arange(1, 19)
print(d)
#[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18]

e = d.reshape(3, 6)
print(e)

#[[ 1  2  3  4  5  6]
#[ 7  8  9 10 11 12]
#[13 14 15 16 17 18]]