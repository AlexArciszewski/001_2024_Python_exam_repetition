# Zadanie 5. Wydrukuj trzy pierwsze elementy tablicy *y*.


import pandas as pd

x = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(x)


y = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(y[:3])


#a    1
#b    2
#c    3
#d    4
#e    5
#dtype: int64

#a    1
#b    2
#c    3
#dtype: int64

