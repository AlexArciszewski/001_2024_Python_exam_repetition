# Zadanie 6. Wydrukuj element odpowiadający indeksowi a oraz b.


import pandas as pd

x = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(x)


# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64


y = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(y[:3])

# a    1
# b    2
# c    3
# dtype: int64

x = y[:2]
print(x.values)

# [1 2]

print(y[:2].values)

# [1 2]


print(y[['a', 'b']])

# a    1
# b    2

