#Tablice można jak macierze doddawac,mnożć ,transponowac, srpawdzac rozmaiar np.size()
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 1, 1], [2, 2, 2]])

print(a+b)

#[[2 3 4]
# [6 7 8]]

print(a-b)

#[[0 1 2]
# [2 3 4]]

#mnożenie elemntów przez siebie nie tak jak w macierzach
print(a*b)
#[[ 1  2  3]
# [ 8 10 12]]

#Mnozenie matematyczne funkcja np.matmul w drugim wierszy co w pierwszym kolumn musi być
#to da bląd
#print(np.matmul(a, b))


a = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(np.matmul(a, c))
#[[14 14 14]
# [32 32 32]]


#transponowanie tablic a.T

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.T)

#[[1 4]
# [2 5]
# [3 6]]

#Rozmiar tablicy np.size() zwracaj liczbę elementów

a = np.array([[1, 2, 3], [4, 5, 6]])

print(np.size(a))

#6


#Sprawdzenie warunkuc zy dane liczby z tablicy  spełniają tenw arunek

a = np.array([[1, 2, 3], [4, 5, 6]])

print(a>2)


#[[False False  True]
# [ True  True  True]]