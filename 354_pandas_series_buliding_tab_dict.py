# Zadanie 4. Zbuduj dokładnie taką samą tablicę jak wyżej używając słownika. Przypisz tablicę do zmiennej *y*.


import pandas as pd

x = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(x)


y = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(y)


#a    1
#b    2
#c    3
#d    4
#e    5
#dtype: int64