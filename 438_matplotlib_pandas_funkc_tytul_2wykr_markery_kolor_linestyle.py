import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


df =pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx')


print(df.head())
df['Data'] = pd.to_datetime(df['Data'])
print(df.info())
#przypisanie dnaych
x=df['Data']
y=df['Wynik finansowy']
#wykresy i ich opis oraz wlasciwosci
plt.plot(x,y, marker='o', linestyle='--', color='b',linewidth=5,  label='Wynik finansowy')   #można użyć hex string za kolor
plt.plot(x, df['Przychody'],marker='x', color='r', label='Przychody')
#markery->, _ o x + - X D - 


#opisy osi
plt.xlabel('Data')
plt.ylabel('Wynik finansowy')
#tytuł wykresu
plt.title('Wynik finansowy organizacji')
#legenda
plt.legend(loc=2)
plt.show()