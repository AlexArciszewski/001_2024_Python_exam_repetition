#sieriest tablice jednowymairowe ale sieries posiadają etykiety wierszy, ktore mogą byc dowolne

import pandas as pd


#Tworzenie series


#1.bezposrednio na podstawie list lub iterowalnego obiektu

series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(series)

#a    1
#b    2
#c    3
#d    4
#e    5
#dtype: int64


#2.slownik


series2 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(series2)

#a    1
#b    2
#c    3
#d    4
#e    5
#dtype: int64

#dodawanie elementu


series2['f'] = 999
print(series2)

#a      1
#b      2
#c      3
#d      4
#e      5
#f    999
#dtype: int64

#zmiana elementu etykeity

series2['a1'] = series2.pop('a')


print(series2)

#b       2
#c       3
#d       4
#e       5
#f     999
#a1      1
#dtype: int64



#usuniecie elementów
series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
x = series.drop(['a'])
print(x)

#b    2
#c    3
#d    4
#e    5
#dtype: int64


#wykorzystanie funkcji min, max,where