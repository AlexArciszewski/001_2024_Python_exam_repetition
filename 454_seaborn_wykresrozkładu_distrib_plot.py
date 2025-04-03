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


#Tworzymy wykres

sns.displot(df['total_bill'], kde=True)
plt.show()
#jako argument podając dane, których rozkład chcemy przedstawić i opcjonalny argument kde=True, 
# dzięki któremu widzimy jak kształtuje się teoretyczny rozkład danych.

#Na naszym wykresie występuję zauważalna asymetria prawostronna, co oznacza, że większość osób miało rachunek niższy, niż przeciętny rachunek.
#spłaszczenie rozkładu. Im wyższy „dzwon” tym wartości są bardziej skupione wokół średniej. Im bardziej spłaszczony dzwon, tym obserwacje są mniej skupione wokół średniej.
#Na podstawie powyższego histogramu możemy również odczytać, że najwięcej osób miało rachunek od 10 do 20 dolarów, oraz że najwyższy rachunek wynosił około 50 dolarów.
#sns.displot(df['total_bill'], kde=True, bins=10) bins=10 prostokątów zostanie wyświetlone.