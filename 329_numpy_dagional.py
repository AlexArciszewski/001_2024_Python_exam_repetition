# Zadanie
    # W algebrze macierzy elementem neutralnym jest macierz zer, wypełniona jedynkami na przekątnej.
    # Do zmiennej diag zapisz macierz o takich wymiarach jak X i wypełnioną samymi zerami (skorzystaj z zeros())
    # Wypełnij diag jedynkami na przekątnej. (Skorzystaj z fill_diagonal()
    # Pomnóż przez siebie X i diag i sprawdź czy wynik to X. (Skorzystaj z dot())

import numpy as np


X = np.arange(1, 26)
print(X)
X = X.reshape(5, 5)
print(X)

diag = np.zeros(X.shape)
print(diag)

# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

print('\n')

#wypełnienie jedynkami


np.fill_diagonal(diag, 1)
print(diag)

# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

print('\n')
Y = np.dot(X, diag)
print(Y)

# [[ 1.  2.  3.  4.  5.]
#  [ 6.  7.  8.  9. 10.]
#  [11. 12. 13. 14. 15.]
#  [16. 17. 18. 19. 20.]
#  [21. 22. 23. 24. 25.]]