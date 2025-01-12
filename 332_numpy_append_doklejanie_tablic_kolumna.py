#Zadanie
#Oto dwie tablice:
import numpy as np
x = np.array([[10,20,30], [40,50,60]])
y = np.array([[100], [200]])

#Dodaj (a właściwie doklej) do tablicy x tablicę y jako nową kolumnę. (Skorzystaj z append() z parametrem axis=1)

print(np.append(x, y, axis=1))

# [[ 10  20  30 100]
#  [ 40  50  60 200]]