import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/data_csv.csv')

print(df.head())

df.info()
df['Date'] = pd.to_datetime(df['Date'])
df.info()

x = df['Date']
y = df['SP500']

# plt.plot(x, y)
# plt.show()


plt.bar(x, y, width=33)
plt.show()