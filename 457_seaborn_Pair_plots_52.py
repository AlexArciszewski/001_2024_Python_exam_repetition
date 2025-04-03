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

sns.pairplot(df)
plt.show()

# Pair Plots to bardzo często używane narzędzie przez każdego analityka danych. Za ich pomocą tworzą się wykresy obrazujące zależności między każdą parą zmiennych 
# ilościowych znajdujących się w naszym zbiorze danych.
#zostały wyróżnione trzy zmienne: total_bill, tip oraz size. Wszystkie te zmienne są ilościowe. Na głównej przekątnej znajdują się histogramy, 
# ponieważ na głównej przekątnej znajdują się zależności między tymi samymi zmiennymi.
# Poza przekątną znajdują się wykresy rozrzutu, dzięki którym możemy odczytać jakie zależności zachodzą między zmiennymi. Na przykład między wysokością napiwku a całkowitą 
# kwotą za posiłek występuję dodatnia, dość silna zależność.

#Możemy urozmaicić te wykresy za pomocą argumentu hue, który definiuje w podziale na jaką zmienną kategoryczną mają zostać wykonane te wykresy

sns.pairplot(df, hue='sex')
plt.show()

#kolory arg palette

sns.pairplot(df, hue='sex', palette='Blues')
plt.show()
