import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx', engine='openpyxl')
print(df.head())
print(df.info())
df['Data'] = pd.to_datetime(df['Data'])
print(df.info())




x=df['Data']
y=df['Liczba pracowników']
plt.plot(x,y)
plt.title('Rozkład liczby pracowników w czasie')
plt.xlabel('Data')
plt.ylabel('Liczba pracowników')


plt.savefig('wykres001.jpg')
plt.show()