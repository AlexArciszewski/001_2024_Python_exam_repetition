#dwuwymairowe nd.arrays


import numpy as np
import pandas as pd

x = np.array([['Mazowieckie', 'Warszawa', 5.42],
            ['Warminsko-Mazurskie', 'Olsztyn', 	1.42],
            ['Podlaskie', 'Białystok', 	1.18],
            ['Pomorskie', 'Gdańsk', 	2.35],
            ['Małopolskie', 'Kraków', 	3.41]]
        )


df = pd.DataFrame(x)
print(df)



#                     0          1     2
#0          Mazowieckie   Warszawa  5.42
#1  Warminsko-Mazurskie    Olsztyn  1.42
#2            Podlaskie  Białystok  1.18
#3            Pomorskie     Gdańsk  2.35
#4          Małopolskie     Kraków  3.41

print("\n oznaczenie  kolumn \n")

df = pd.DataFrame(x, columns = ['wojewodztwo','stolica','l_ludnosci'])
print(df)

#           wojewodztwo    stolica l_ludnosci
#0          Mazowieckie   Warszawa       5.42
#1  Warminsko-Mazurskie    Olsztyn       1.42
#2            Podlaskie  Białystok       1.18
#3            Pomorskie     Gdańsk       2.35
#4          Małopolskie     Kraków       3.41

print("\n indeksy \n")

df = pd.DataFrame(x, columns = ['wojewodztwo','stolica','l_ludnosci'], index = ['MAZ', 'WM', 'POD', 'POM', 'MAL'])
print(df)


#             wojewodztwo    stolica l_ludnosci
#MAZ          Mazowieckie   Warszawa       5.42
#WM   Warminsko-Mazurskie    Olsztyn       1.42
#POD            Podlaskie  Białystok       1.18
#POM            Pomorskie     Gdańsk       2.35
#MAL          Małopolskie     Kraków       3.41