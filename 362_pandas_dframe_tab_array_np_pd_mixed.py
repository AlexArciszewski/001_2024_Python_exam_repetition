#Zadanie 3. Stwórz *ndarray*, który ma wyglądać w następujący sposób:

# [[10 10 10]
#  [20 20 20]
#  [30 30 30]]

#Po czym na podstawie tego *ndarray* stwórz *df*, które będzie wyglądało w następujący sposób:
#    k1  k2  k3
# w1  10  10  10
# w2  20  20  20
# w3  30  30  30

#Nazwij tą tabelę:tablica

import numpy as np
import pandas as pd

my_tab = np.array([[10, 10, 10], [20, 20, 20], [30, 30, 30]])
print(my_tab)

tablica = pd.DataFrame(my_tab, columns=['k1', 'k2', 'k3'], index=['w1', 'w2', 'w3'])
print(tablica)