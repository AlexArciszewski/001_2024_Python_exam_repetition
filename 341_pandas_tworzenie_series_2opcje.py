import pandas as pd

m = pd.Series([1, 2, 3, 4, 5])
print(m)

#0    1
#1    2
#2    3
#3    4
#4    5
#dtype: int64


#nadpisane indeksów zmiana na takie jakie chcemy


x = pd.Series([1, 2, 3, 4, 5] , index=['a', 'b', 'c', 'd', 'e'])
print(x)


#a    1
#b    2
#c    3
#d    4
#e    5
#dtype: int64


print(x.index)

#Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

print(x.values)
#[1 2 3 4 5]


#Opcja nr2
y = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(y)


#a    1
#b    2
#c    3
#d    4
#e    5
#dtype: int64

