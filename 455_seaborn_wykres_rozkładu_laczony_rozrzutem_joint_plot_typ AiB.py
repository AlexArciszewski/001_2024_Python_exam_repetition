#wykres rozkładu (distribution plot) pozwala na wizualizację rozkładu danych porównując empiryczny rozkład danych z teoretycznym rozkładem danych.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())


#Tworzymy wykres typu A

sns.jointplot(x='total_bill',y='tip', data=df)
plt.show()
# X – pierwsza zmienna, jaka ma być na wykresie
# • Y – druga zmienna, jaka ma być na wykresie
# • Data – nazwa (z reguły DataFrame’u) gdzie znajdują się nasze zmienne
# • Kind – rodzaj wykresu, jaki ma być narysowany w środku. Kilka podstawowych typów to między innymi: scatter – wykres rozrzutu (domyślny), hist – histogram, reg – regresja
#sns.jointplot(x='total_bill',y='tip', data=df, kind='reg')  linia regresji

# Gdy chcemy bliżej poznać rozkłady interesujących nas zmiennych oraz zależności między tymi zmiennymi. 
# Z powyższego wykresu możemy odczytać, że total_bill charakteryzuje się asymetrią prawostronną, zmienna tip charakteryzuje się asymetrią lewostronną, 
# za to zależność między zmiennymi jest dodatnia (ponieważ wraz ze wzrostem jednej zmiennej druga zmienna również rośnie).



#Tworzymy wykres typu B
sns.jointplot(x='total_bill',y='tip', data=df, kind='hist')
plt.show()

#Wykres ten prezentuje histogramy obu zmiennych oraz histogram zbiorczy (im ciemniejszy kolor tym suma wartości z poszczególnych histogramów jest większa).





