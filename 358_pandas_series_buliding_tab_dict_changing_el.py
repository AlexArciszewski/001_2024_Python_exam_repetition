# Zadanie 8. Zmień indeks "d" na "xyz".

#W przypadku y['xyz'] = y.pop('d') najpierw usuwamy wartość przypisaną do 'd' (czyli 4), a następnie przypisujemy ją do
# 'xyz'. Użycie pop() jest więc wygodne w przypadku operacji usuwania i przypisywania jednocześnie,
# podczas gdy zwykłe przypisanie (np. y['a'] = 100) służy tylko do zmiany wartości w istniejącym kluczu.

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

y['a'] = 100

print(y[['a', 'b']])

# a    100
# b      2
# dtype: int64


y['xyz'] = y.pop('d')
print(y)

# a      100
# b        2
# c        3
# e        5
# xyz      4
# dtype: int64


















