#Utwórz tablicę diagonal_array o wymiarach 5x5, która na przekątnej ma jedynki, a pozostałe wartości to zera.
# Hint: Skorzystaj z metody eye
import numpy as np

diagonal_array = np.eye(5)
print(diagonal_array)

#[[1. 0. 0. 0. 0.]
# [0. 1. 0. 0. 0.]
# [0. 0. 1. 0. 0.]
# [0. 0. 0. 1. 0.]
#[0. 0. 0. 0. 1.]]