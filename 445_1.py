import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df =pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx')

print(df.head())
df.info()

df['Data'] = pd.to_datetime(df['Data'])
df.info()
df['Data_str'] = df['Data'].apply(lambda x:x.strftime("%Y-%m"))

x=df['Data']
y=df['Wynik finansowy']
x2 = df['Data_str']

plt.style.use('ggplot')

plt.plot(x2, y, marker='o', linestyle='--', color='b', linewidth=2, label='Wynik')
plt.plot(x2, df['Przychody'], marker='x', color='r', label='Przychody')

plt.yticks([-400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800])
plt.xticks(['2014-01','2015-09'], rotation=45)

plt.xlabel('Data')
plt.ylabel('Wynik finansowy')

plt.title('Wynik finansowy organizacji')
plt.text('2014-01', 600, 'wykres', color='b', size=24)

plt.legend(loc=2)
plt.grid(True)
plt.show()
