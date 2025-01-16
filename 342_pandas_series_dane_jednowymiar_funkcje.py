# wartości liczbowe dla zbioru liczb funkcje pomagają w oblcizeniach. Funkcja z numpy where
import numpy as np
import pandas as pd


y = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(y)



print(y.min())
#1
print(y.max())
#5
print(y.mean())
#3.0
print(y.std())
#1.5811388300841898

# Funkcja where warunek,co ma zwrócic jak jest ok, co ma zwórcić jak warunek nei jest spelniony
print(np.where(y > 3, y, 'False'))
# ['False' 'False' 'False' '4' '5']