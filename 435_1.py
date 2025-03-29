import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx', engine='openpyxl')

print(df.head())
print(df.info())


df['Data'] = pd.to_datetime(df['Data'])
print(df.info())

x = df['Data']
y = df['Wynik finansowy']

plt.plot(x, y, label='Wynik finansowy')
plt.title('Wynik finansowy przesiębiorstwa')
plt.xlabel('Data')
plt.ylabel('Wynik finansowy')

plt.plot(x, df['Przychody'], label='Przychody')


plt.legend(loc=1)
plt.savefig('wyk02.jpg')
plt.show()
 