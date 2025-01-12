#Oto dwie tablice:

import numpy as np
x = np.array([[10, 20, 30], [40, 50, 60]])
y = np.array([[100, 200, 300]])

#Dodaj (a właściwie doklej) do tablicy x tablicę y, jako nowy wiersz

print(np.append(x,y ,axis=0))

# [[ 10  20  30]
#  [ 40  50  60]
#  [100 200 300]]