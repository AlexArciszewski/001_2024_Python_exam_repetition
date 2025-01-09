#Zadanie 1. Stwórz *series* składającą się z liczb od 5 do 10. Przypisz nazwy indeksów "a,b,c,d,e,f".
# Przypisz tą tablicę do zmiennej *x* (nie używaj słownika).
import pandas as pd

x = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(x)


#a    1
#b    2
#c    3
#d    4
#e    5
#dtype: int64