#Where zwraca elementy spełnaijace okresloen warunki
#przyjmuje 3 argumenty  1-warunek to spełnienia 2-akcja do wykonania w przypadku spelnienia
# warunku 3-akcja jesli warunek nie jest spelniony


import numpy as np


c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


#Dla elementu mniejszego lub równego 3 zwrócimy element z tablicy w innym razie False
print(np.where(c <= 3, c, "False"))

#[['1' '2' '3' 'False']
#['False' 'False' 'False' 'False']
#['False' 'False' 'False' 'False']]



#Dla elementu mniejszego lub równego 3 zwrócimy element z tablicy w innym razie False
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(np.where(c <= 3, c, c * 2))


#[[ 1  2  3  8]
# [10 12 14 16]
# [18 20 22 24]]