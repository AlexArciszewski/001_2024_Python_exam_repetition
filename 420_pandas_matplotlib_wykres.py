import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx')
df = pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx', engine='openpyxl')
print(df.head())
print(df.info())
#zmiana typu danych dla kolumny Data jestobject a musi być datetime aby miećdaty a nie tekst

df['Data'] = pd.to_datetime(df['Data'])

print(df.info())


print(df.plot('Data','Wynik finansowy'))
print(plt.show())