#Wyświetl tablicę o wymiarach takich jak X, gdzie (we wszystkich punktach korzystaj z where):
    #występują tylko jedynki i zera. Jedynki mają się pojawić tam, gdzie w X występuje wartość większa od 10,
    # a zero w pozostałych przypadkach
    #występują tylko jedynki i zera. Jedynki mają się pojawiać tam, gdzie w X występuje wartość parzysta,
    #  a zero w pozostałych przypadkach
    #występują tylko liczby parzyste. Jeśli w X wartość była parzysta, to należy ją przepisać.
    # Jeśli była nieparzysta , to dodać 1

import numpy as np


X = np.arange(1, 26)
print(X)
X = X.reshape(5, 5)
print(X)

# [[ 1  2  3  4  5]
# [ 6  7  8  9 10]
# [11 12 13 14 15]
# [16 17 18 19 20]
# [21 22 23 24 25]]

#występują tylko jedynki i zera. Jedynki mają się pojawić tam, gdzie w X występuje wartość
# większa od 10 a zero w pozostałych przypadkach

y = np.where(X > 10, 1, 0)
print(y)

# [[0 0 0 0 0]
#  [0 0 0 0 0]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]


#występują tylko jedynki i zera. Jedynki mają się pojawiać tam, gdzie w X występuje wartość parzysta,
    #  a zero w pozostałych przypadkach

Z = np.where(X % 2 == 0, 1, 0)
print(Z)

# [[0 1 0 1 0]
#  [1 0 1 0 1]
#  [0 1 0 1 0]
#  [1 0 1 0 1]
#  [0 1 0 1 0]]

#występują tylko liczby parzyste. Jeśli w X wartość była parzysta, to należy ją przepisać.
    # Jeśli była nieparzysta , to dodać 1

W = np.where(X % 2 == 0, X, X+1)
print(W)

# [[ 2  2  4  4  6]
#  [ 6  8  8 10 10]
#  [12 12 14 14 16]
#  [16 18 18 20 20]
#  [22 22 24 24 26]]