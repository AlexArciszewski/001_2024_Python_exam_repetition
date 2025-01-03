#Zadanie 4. Zbuduj tablicę jednowymiarową zawierającą liczby od 10 do 20.
import numpy as np

#Sprawdź za pomocą odpowiednich funkcji, jakie jest:

#a) minimum tablicy
#b) maksimum tablicy
#c) średnia elementów z tablicy
#d) suma elementów z tablicy

my_array = np.arange(10, 21)
print(my_array)


print(min(my_array))
#10

print(max(my_array))
#20

print((my_array.mean()))
#15.0

print(sum(my_array))
#165

print(my_array.sum())
#165




