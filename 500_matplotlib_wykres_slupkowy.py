#Zadanie
#Narysuj następujący wykres korzystając z biblioteki *matplotlib*:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df1 = sns.load_dataset('exercise')
df2 = sns.load_dataset('mpg')
df3 = sns.load_dataset('tips')

print(df1.head())

plt.bar(df1['diet'].unique(), df1['diet'].value_counts())
plt.ylabel('Ilość osob')
plt.xlabel('Typ diety')
plt.title('Rozkład czynnosci zmiennej diety')
plt.show()


#df1['diet'].unique() – zwraca unikalne wartości w kolumnie diet, np. ['low fat', 'no fat']. na osi x
#df1['diet'].value_counts() – liczy wystąpienia każdej diety, np. low fat: 50, no fat: 30. na osi y wysokosc slupkow
#plt.bar(...) – rysuje wykres słupkowy (osie: diet na X, liczba osób na Y).

diets = df1['diet'].value_counts()
plt.bar(diets.index, diets.values)

plt.ylabel('Ilość osób')
plt.xlabel('Typ diety')
plt.title('Rozkład liczby osób na różnych dietach')
