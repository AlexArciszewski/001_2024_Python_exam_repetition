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

sns.scatterplot(data=df2, x='weight', y='horsepower')   #przypisanie danych
plt.title('Zależnosć wagi auta od mocy')        #tytul wykresu
plt.ylabel('Moc samochodu')                     #opis osi y
plt.xlabel('Waga samochodu')                    #opis osi x
plt.yticks([50,100,150,200,250,300])            #podzialka y
plt.xticks([1500,2500,3500,4500,5500])          #podzialka x
plt.show()