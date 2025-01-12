# W zmiennej X zapisz tablicę dwuwymiarową z kolejnymi liczbami od 1 do 25. (Skorzystaj z arange() i reshape()

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

# W zmiennej Ones zapisz tablicę o takim samym kształcie 5x5, ale całą wypełnioną tylko jedynkami.
# (Skorzystaj z ones())




Ones = np.ones((5, 5))
print(Ones)
#nawiazanie do shape tab z X

Ones2 = np.ones(X.shape)

# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]


Y = np.dot(X, Ones)

print(Y)

# [[ 15.  15.  15.  15.  15.]
#  [ 40.  40.  40.  40.  40.]
#  [ 65.  65.  65.  65.  65.]
#  [ 90.  90.  90.  90.  90.]
#  [115. 115. 115. 115. 115.]]




