import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


df =pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx')


print(df.head())
print(df.info())
df['Data'] = pd.to_datetime(df['Data'])
print(df.info())


x=df['Data']
y=df['Wynik finansowy']

plt.plot(x, y, marker='o', color='b', label='Wynik finansowy')

plt.xlabel('Data')
plt.ylabel('Wynik finansowy')

plt.title('Wynik firmy')

plt.legend(loc=1)


plt.show()
