#Zadanie
#Narysuj następujący wykres korzystając z biblioteki *matplotlib*:



import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df1 = sns.load_dataset('exercise')
df2 = sns.load_dataset('mpg')
df3 = sns.load_dataset('tips')

print(df2.head())



print(df2.describe)


df2.info()
print('\n')


#origin
#sa       249
#japan      79
#europe     70
#Name: count, dtype: int64

#ile kategorii producentow aut w wykresie
values = df2['origin'].value_counts()
print(values)

#nazwy producentow

names = df2['origin'].value_counts().index
print(names)

plt.figure(figsize=(10, 10))
plt.pie(values, labels=names, autopct='%1.2f%%', colors=['pink','blue', 'green'], textprops={'fontsize':14})
plt.title('Rozklad częstości zmiennej origin')
plt.show()