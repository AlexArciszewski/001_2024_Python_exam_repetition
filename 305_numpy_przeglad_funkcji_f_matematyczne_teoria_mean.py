#Funkcje matematyczne

import numpy as np


c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

#minimum
print(c.min())

#1

#max
print(c.max())

#12

#srednia
print(c.mean())


mean_columns = c.mean(axis=0)
print("Średnia dla każdej kolumny:", mean_columns)

#6.5

#suma
print(c.sum())
#78