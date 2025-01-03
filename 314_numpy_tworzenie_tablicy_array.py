#Zadanie 3. Stwórz tablicę o rozmiarze 3x3 składającą się z liczb
#
#10,11,12
#
#13,14,15
#
#16,17,18
#
#po czym dokonaj transformacji, w wyniku której będzie to tablica jednowymiarowa (z jednym wierszem).


import numpy as np

my_array = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print(my_array)

#[[10 11 12]
# [13 14 15]
# [16 17 18]]

reshaped_array = my_array.reshape(1, 9)

print(reshaped_array)

#[[10 11 12 13 14 15 16 17 18]]