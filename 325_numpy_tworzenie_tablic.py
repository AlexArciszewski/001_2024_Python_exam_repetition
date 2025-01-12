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