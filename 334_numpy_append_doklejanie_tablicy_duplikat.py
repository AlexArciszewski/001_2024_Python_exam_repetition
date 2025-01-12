#9. Do tablicy x z poprzedniego punktu, doklej tablicę x jako nowe wiersze (wiersze będą zduplikowane)


import numpy as np
x = np.array([[10,20,30], [40,50,60]])

print(np.append(x, x, axis=0))


# [[10 20 30]
#  [40 50 60]
#  [10 20 30]
#  [40 50 60]]
