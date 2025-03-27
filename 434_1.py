import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx', engine='openpyxl')
print(df.head())
print(df.info())
df['Data'] = pd.to_datetime(df['Data'])
print(df.info())




x=df['Data']
y=df['Wynik finansowy']
plt.plot(x,y, label='Wynik finansowy')
plt.title('Wynik Finansowy przedsiębiorstwa')
plt.xlabel('Data')
plt.ylabel('Wynik finansowy')

#dorzucamy drugi wykres

plt.plot(x,df['Przychody'], label='Przychody')


#dorzucamy trzeci wykres

plt.plot(x, df['Koszty'], label='Koszty')

plt.legend()
plt.savefig('wykres001.jpg')
plt.show()