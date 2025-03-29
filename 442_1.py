import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



df =pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx')


print(df.head())
df['Data'] = pd.to_datetime(df['Data'])
print(df.info())
#przypisanie dnaych
x=df['Data']
y=df['Wynik finansowy']
#styl wykresu
plt.style.use('ggplot')
plt.plot(x, y, marker='o', linestyle='--', color='b', linewidth=10, label= 'Gruby wynik finansowy')
#podziałka
plt.yticks([-400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800])
plt.xticks(rotation=45)

plt.xlabel('Data')
plt.ylabel('Wynik finansowy')
#tytuł wykresu
plt.title('Wynik finansowy organizacji')
#legenda
plt.legend(loc=2)
#siatka
plt.grid(True)
plt.show()

