#aporuszanie sie po tablicach osobono wiersze i kolumny
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

#z tablicy wybieram wiersze o indeksach 1 i 2 oraz kolumny o indeksach 0 i 1
print(a[1:3, :2])

#[[ 5  6]
# [ 9 10]]



#z tablicy wybieramy elementy różne

b = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#pierwsze 2 elementy na pozycji 0 oraz 1
print(b[:2])

#[1 2]

#pierwsze 2 elementy na pozycji 1 oraz 2 bez pozycji 0
print(b[1:3])

#[2 3]

#od pierwszego elementu na pozycji 1 bez tego na pozycji 0 dko końca listy
print(b[1:])

#[2 3 4 5 6 7 8]


#Tablice wielowymiarowe


c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(c)

#wybieramy wszystkie kolumny ale tylko dwa pierwsze wiersze.
print(c[:2, :])

#[[1 2 3 4]
# [5 6 7 8]]


#wybieramy wszystkie kolumny ale tylko dwa pierwsze wiersze.
print(c[:2])

#[[1 2 3 4]
# [5 6 7 8]]

#wiersze od 1 i 2 bez 0 oraz kolumny od 2 do końca z pominieciem 0 i 1
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(c[1:3,:2])

#[[ 5  6]
# [ 9 10]]

#iterowanie petlą po talicach do wypisywania lub podmieniania wartościw  tablicach
#podwójna petla najpierw iterujemy po wierszach później po kolumnach
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

for i in c:
    for j in i:
        print(j)
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10
#11
#12
#terujemy po wierszach wszystko


#Wypisz tylko liczby większe od 5
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


for i in c:
    for j in i:
        if j > 5:
            print(j)

#6
#7
#8
#9
#10
#11
#12


#Sumowanie elementów tablicy
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
suma = 0
for i in c:
    for j in i:
        suma += j
print(suma)

#78


