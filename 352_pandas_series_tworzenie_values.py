# Zadanie 2. Wydrukuj wartości znajdujące się w w tabeli *x*.

import pandas as pd

x = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(x)


#a    1
#b    2
#c    3
#d    4
#e    5
#dtype: int64


print(x.values)
#[1 2 3 4 5]