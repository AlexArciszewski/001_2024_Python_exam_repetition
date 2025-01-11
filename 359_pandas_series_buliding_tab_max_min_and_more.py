# Zadanie 9. Znajdź maksimum tabeli *y*.

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

print(y.max())
# 100

print(y.min())

# 2

print(y.mean())

# 22.8

print(y.std())

# 43.17059184213254



# Metoda median() oblicza medianę serii, czyli wartość, która dzieli zbiór danych na dwie równe części.
# Jeśli masz nieparzystą liczbę elementów, to mediana to środkowa wartość, a jeśli liczba elementów jest parzysta,
# mediana to średnia z dwóch środkowych wartości.



print(y.median())

# 4.0

# Wariancja serii, czyli miarę rozproszenia danych względem średniej. Wariancja mierzy,
# jak bardzo wartości w zbiorze różnią się od średniej. Wyższa wariancja oznacza większe rozproszenie danych.

print(y.var())




# 1863.7000000000003



# Metoda quantile() oblicza wartości w określonych punktach rozkładu, które odpowiadają zadanym kwantylom.
# Kwantyle dzielą zbiór danych na części, z których każda zawiera określoną część wartości. Na przykład:

    # Kwantyl 0.5 to mediana (50% danych).
    # Kwantyl 0.1 to wartość, poniżej której znajduje się 10% danych.
    # Kwantyl 0.9 to wartość, poniżej której znajduje się 90% danych.


print(y.quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]))

# 0.1     2.4
# 0.2     2.8
# 0.3     3.2
# 0.4     3.6
# 0.5     4.0
# 0.6     4.4
# 0.7     4.8
# 0.8    24.0
# 0.9    62.0
# dtype: float64










