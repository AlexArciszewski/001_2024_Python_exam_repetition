#Utwórz tablicę X_bis wyznaczoną w następujący sposób. Dla wartości w X większych od 10 zwrócona jest wartość 2 razy
# większa, a dla pozostałych 0. Policz ile jest elementów niezerowych w X_bis (skorzystaj z count_nonzero())


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



X_bis = np.where(X > 10, 2*X, 0)
print(X_bis)

# [[ 0  0  0  0  0]
#  [ 0  0  0  0  0]
#  [22 24 26 28 30]
#  [32 34 36 38 40]
#  [42 44 46 48 50]]

print(np.count_nonzero(X_bis))
#15