#Modyfikacja Series
import pandas as pd


y = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(y)


#a    1
#b    2
#c    3
#d    4
#e    5
#dtype: int64

#Dodanei etykiety

y['f'] = 6

print(y)

#a    1
#b    2
#c    3
#d    4
#e    5
#f    6
#dtype: int64



w = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

w['aa'] = w.pop('a')
print(w)

#Znika wiersz z etykieta a i pojawia sie aa tyle ze na koncu
#b     2
#c     3
#d     4
#e     5
#aa    1
#dtype: int64

#usuwanie etykiety trzeba prypsiac do innej zmiennej dane bo w zostaje niezmienione.
u = w.drop(['b'])
print(u)

#c     3
#d     4
#e     5
#aa    1
#dtype: int64


#usuwanie na oryginalnych danych

print(y)

#a    1
#b    2
#c    3
#d    4
#e    5
#f    6
#dtype: int64


y.drop(['a'], inplace=True)
print(y)


#b    2
#c    3
#d    4
#e    5
#f    6
#dtype: int64

