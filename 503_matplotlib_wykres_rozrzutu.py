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

sns.scatterplot(data=df2, x='acceleration', y='horsepower', marker ='x')   #przypisanie danych i marker
plt.title("Zależność między przyspieszeniem a mocą samochodu")        #tytul wykresu
plt.ylabel('Moc samochodu')                     #opis osi y
plt.xlabel('Przyspieszenie')                    #opis osi x
plt.yticks([50, 75, 100, 125, 150, 175, 200, 225, 250])            #podzialka y
plt.xticks([7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0])          #podzialka x
plt.show()