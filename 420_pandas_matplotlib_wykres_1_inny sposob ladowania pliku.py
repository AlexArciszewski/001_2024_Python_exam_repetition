import numpy as np 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


# df = pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx',engine='openpyxl')
# print(df.head())

with pd.ExcelFile('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx',engine='openpyxl') as xls:
      print(xls.sheet_names)  # Lista arkuszy
      df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])  # Wczytaj pierwszy arkusz

print(df)
print(df.info())
#trzeba przeformatować Date z object na datetime
df['Data'] = pd.to_datetime(df['Data'])
print(df.info())
print(df.plot('Data', 'Wynik finansowy'))
plt.show()