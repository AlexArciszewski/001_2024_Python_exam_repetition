# Pytanie 14
# Wypisz pierwsze 5 elementów listy L.
# Wypisz co drugą literę stringa s, zaczynając od ostatniej i cofając się do poczatku.

L = [11, 22, 33, 44, 55, 66, 77, 88, 99, 1010]
s = 'a nMozh^tKysPW 9ęxi b$uML'
print(L[0:5])
print(s[::-2])
print(s[-1::-2])
# od ostatniego -1 do końca czyli do pierwszego : ze skokiem -2 co drugi
# [11, 22, 33, 44, 55]
# Lubię Pythona