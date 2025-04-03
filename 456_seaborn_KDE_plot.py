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

print(plt.hist(df['tip']))

#    total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4
# (array([41., 79., 66., 27., 19.,  5.,  4.,  1.,  1.,  1.]), array([ 1. ,  1.9,  2.8,  3.7,  4.6,  5.5,  6.4,  7.3,  8.2,  9.1, 10. ]), <BarContainer object of 10 artists>)

plt.hist(df['tip'])
plt.show()

#nieco zmieniony histogram ->tj posypany piaskiem
sns.kdeplot(df['tip'])
plt.show()



# Wykres kde plot tworzymy używając funkcji sns.kdeplot(). Kde plot z kilku powodów są lepsze od histogramów:
# • Podczas szatkowania danych w bins możemy utracić ważne informacje na temat rozkładu. Kde plot zawsze podaje unikalne 
# wartości dla konkretnego rozkładu i przedziału.
# • Kde plot są gładsze, co ułatwia późniejsze przetwarzanie tego wykresu