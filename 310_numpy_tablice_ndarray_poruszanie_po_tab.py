import numpy as np

# Zadanie 1. Stwórz tablicę *a* o wymiarze 3x3 składającą się z liczb 1,2,3 i 4,5,6 i 7,8,9.

a = np.array([[1, 2, 3,], [4, 5, 6], [7, 8, 9]])
print(a)

#Zadanie 2. Za pomocą indeksowania wydrukuj liczby 1,2,3.
print(a[0])

#[1 2 3]


#Zadanie 3. Za pomocą indeksowania wydrukuj liczby 3,6,9.

print(a[0][2], a[1][2], a[2][2])
print(a[:,2])


#3 6 9
#[3 6 9]

#Zadanie 4. Za pomocą indeksowania wydrukuj liczby 1,4,7.

a = np.array([[1, 2, 3,], [4, 5, 6], [7, 8, 9]])

print(a[:, 0])

#[1 4 7]

#Zadanie 5. Za pomocą indeksowania wydrukuj liczby 7,8,9.

print(a[2])
#[7 8 9]


#Zadanie 6. Za pomocą indeksowania wydrukuj liczby 1,2 4,5.
print(a[:2, :2])

#[[1 2]
# [4 5]]


#Zadanie 7. Za pomocą pętli for wydrukuj wszystkie elementy składające się na tablicę *a*

for el in a:
    print(el)

#[1 2 3]
#[4 5 6]
#[7 8 9]

for el in a:
    for num in el:
        print(num)

#liczby od 1 do 9


#Zadanie 8. Wydrukuj tylko te elementy tablicy *a*, które są większe od 5 (skorzystaj z pętli *for*).

for el in a:
    for num in el:
        if num >5:
            print(num)
#liczby6789

#Zadanie 9. Wypisz wszystkie elementy tablicy *a* w taki sposób, że wszystkie elementy mniejsze od 4 mają być zamienione na liczbę 10.
# (Wskazówka: skorzystaj z pętli *for*).


for el in a:
    for num in el:
        if num < 4:
            num = 10
        print(num)

#101010456789


#Zadanie 10. Wydrukuj iloczyn wszystkich liczb, z których składa się tablica *a*.

import math

a = np.array([[1, 2, 3,], [4, 5, 6], [7, 8, 9]])
print(a)

num_list = []
for el in a:
    for num in el:
        num_list.append(num)
result = math.prod(num_list)
print(result)

result = 1
for el in a:
    for num in el:
        result *= num
        #result = result * num
print(result)