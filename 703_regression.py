import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
%matplotlib inline
# numpy – operacje na macierzach/tablicach, tu do nowej tablicy z wagą ciała nowych zwierząt.
# pandas – do pracy z tabelą danych (DataFrame).
# matplotlib.pyplot – wykresy (scatter plot + linia regresji).
# sklearn.linear_model.LinearRegression – gotowy model regresji liniowej.
# %matplotlib inline – wyświetlanie wykresów bezpośrednio w notebooku (w PyCharm/VSC niepotrzebne).







animals_data = pd.read_csv(r"C:\Dane\2_ML_Projekty\004_ML kurs 001 regresja bazy\animals\animals.csv")
animals_data.info()
animals_data.head()
animals_data.tail()
animals_data.describe()

# info() — informacje o kolumnach, brakach danych.
# head() — pierwsze 5 wierszy.
# tail() — ostatnie 5 wierszy.
# describe() — statystyki liczbowe (średnia, min, max itp.).



animals_data = animals_data[animals_data["name"].isin(["Cow","Goat", "Donkey", "Horse", "Giraffe", "Kangaroo","Rabbit","Sheep","Mole","Pig"])]
# Zostawiasz tylko 10 wybranych zwierząt, reszta jest odrzucana.
# Dlaczego? Aby uprościć dane do analizy tylko dla tych zwierząt.

#animals_data                                        

lr = LinearRegression()
# Tworzysz pusty model regresji liniowej (jeszcze nic nie nauczony)

lr.fit(X=animals_data["body"].values.reshape(-1,1), y=animals_data["brain"].values)
# Tu uczysz model, aby przewidywał wagę mózgu na podstawie masy ciała.
# X – zmienna wejściowa: masa ciała (body).
# .reshape(-1,1) – zamienia wektor na kolumnę (wymóg scikit-learn).
# y – zmienna wyjściowa: masa mózgu (brain).
# Model teraz wie, jaka jest statystyczna zależność: body → brain.

brain_pred =lr.predict(X=animals_data["body"].values.reshape(-1,1))
# Przewidujesz masę mózgu dla wszystkich danych (body), które użyłeś do trenowania.
# W wyniku dostajesz prostą linię regresji

plt.figure(figsize=(7, 5))
plt.scatter(animals_data["body"], animals_data["brain"],color="blue" )
plt.plot(animals_data["body"], brain_pred, color="red", linewidth=2)
#wykres
    # kropki (blue) – prawdziwe dane (body vs brain),
    # linia (red) – przewidywania modelu = linia regresji.

new_animals_body = np.array([100, 200, 300, 400])
new_animals_brain = lr.predict(new_animals_body.reshape(-1,1))
new_animals_brain
#Tworzysz nowe dane wejściowe (masa ciała 100, 200, 300, 400 kg) i liczysz ich przewidywaną masę mózgu wg modelu.

plt.figure(figsize=(7,5))
plt.scatter(animals_data["body"],animals_data["brain"], color="blue")
plt.plot(animals_data["body"], brain_pred, color="red", linewidth=2)
plt.scatter(new_animals_body, new_animals_brain, color ="orange", s=100)
#Dodajesz do wykresu nowe punkty w kolorze pomarańczowym (orange) – to prognozy dla mas 100, 200, 300, 400 kg.

print(lr.coef_)
print(lr.intercept_)
# coef_ – nachylenie prostej (ile rośnie masa mózgu, gdy rośnie ciało o 1 kg),
# intercept_ – punkt przecięcia osi Y (przewidywana masa mózgu dla masy ciała = 0 kg).


r2 = r2_score(animals_data["brain"], brain_pred)
print(f"R² = {r2:.2f}")
# R² mierzy, jak dobrze model regresji liniowej dopasował się do danych.
# Mówi nam: ile procent zmienności zmiennej zależnej (np. masa mózgu) wyjaśnia zmienna niezależna (np. masa ciała).
