import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx')


print(df.head())
print(df.info())
df['Data'] = pd.to_datetime(df['Data'])
print(df.info())

#przypisanie danych
x = df['Data']
y = df['Wynik finansowy']

#wykresy i ich opis
plt.plot(x, y, marker='o', label='Wynik finansowy')
plt.plot(x, df['Przychody'], marker='x', label='Przychody')

#osie
plt.xlabel('Data')
plt.ylabel('Wynik finansowy')

#tytul
plt.title('Wynik finansowy')
#legenda
plt.legend(loc=3)
plt.show()

