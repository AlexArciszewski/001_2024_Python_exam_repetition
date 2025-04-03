import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())


#Tworzymy wykres

sns.scatterplot(data=df, x='total_bill', y='tip')
plt.show()
# X – pierwsza zmienna, jaka ma być na wykresie
# • Y – druga zmienna, jaka ma być na wykresie
# • Data – nazwa (z reguły DataFrame’u) gdzie znajdują się nasze zmienne