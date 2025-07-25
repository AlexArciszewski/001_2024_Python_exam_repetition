import numpy as np                      # Operacje na macierzach, tablicach (tu np. reshape, nowe dane)
import pandas as pd                     # Praca z danymi w formie tabeli (DataFrame)
import matplotlib.pyplot as plt         # Tworzenie wykresów (scatter, linia regresji)
from sklearn.linear_model import LinearRegression  # Model regresji liniowej
from sklearn.metrics import r2_score    # Miara dopasowania modelu (R²)
from sklearn.model_selection import train_test_split  # Podział danych na treningowe i testowe
#%matplotlib inline                      # Dla notebooków – wyświetlanie wykresów w środku notatnika

# Wczytanie danych z pliku CSV
animals_data = pd.read_csv(r"C:\Dane\2_ML_Projekty\004_ML kurs 001 regresja bazy\animals\animals.csv")

# Filtrowanie danych – wybieramy tylko 10 konkretnych zwierząt
animals_data = animals_data[animals_data["name"].isin(
    ["Cow","Goat", "Donkey", "Horse", "Giraffe", "Kangaroo","Rabbit","Sheep","Mole","Pig"]
)]

# Przygotowanie danych:
X = animals_data["body"].values.reshape(-1,1)  # Zmienna niezależna (masa ciała) – reshape wymagane przez scikit-learn
y = animals_data["brain"].values               # Zmienna zależna (masa mózgu)

# Podział danych: 70% do treningu, 30% do testowania modelu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Tworzenie modelu regresji liniowej
lr = LinearRegression()

# Trenowanie modelu tylko na danych treningowych
lr.fit(X_train, y_train)

# Predykcje modelu:
brain_pred_train = lr.predict(X_train)   # Przewidywanie wyników dla danych treningowych
brain_pred_test = lr.predict(X_test)     # Przewidywanie wyników dla danych testowych

# Obliczenie i wyświetlenie współczynnika determinacji R² dla obu zestawów
r2_train = r2_score(y_train, brain_pred_train)  # Jakość dopasowania na danych treningowych
r2_test = r2_score(y_test, brain_pred_test)    # Jakość dopasowania na danych testowych

print(f"R² (train) = {r2_train:.2f}")   # Wynik R² dla zbioru treningowego
print(f"R² (test) = {r2_test:.2f}")     # Wynik R² dla zbioru testowego

# Wykres: dane treningowe i testowe + linia regresji
plt.figure(figsize=(7,5))
plt.scatter(X_train, y_train, color="blue", label="Train data")      # Punkty: dane treningowe
plt.scatter(X_test, y_test, color="green", label="Test data")        # Punkty: dane testowe
plt.plot(X_train, brain_pred_train, color="red", linewidth=2, label="Regression line (Train)")  # Linia regresji
plt.legend()                     # Legenda do wykresu
plt.xlabel("Body weight")         # Etykieta osi X
plt.ylabel("Brain weight")        # Etykieta osi Y
plt.title("Linear Regression: Train vs Test")  # Tytuł wykresu
plt.show()                        # Wyświetlenie wykresu

# Nowe dane: przewidywanie dla nowych mas ciała zwierząt
new_animals_body = np.array([100, 200, 300, 400])             # Nowe dane wejściowe (masa ciała)
new_animals_brain = lr.predict(new_animals_body.reshape(-1,1)) # Przewidywanie masy mózgu na podstawie modelu
print("New animals brain predictions:", new_animals_brain)     # Wyświetlenie przewidywanych wartości

# Wykres: dane treningowe, testowe i nowe przewidywane punkty
plt.figure(figsize=(7,5))
plt.scatter(X_train, y_train, color="blue", label="Train data")         # Dane treningowe
plt.scatter(X_test, y_test, color="green", label="Test data")           # Dane testowe
plt.plot(X_train, brain_pred_train, color="red", linewidth=2, label="Regression line (Train)")  # Linia regresji
plt.scatter(new_animals_body, new_animals_brain, color="orange", s=100, label="New predictions")  # Nowe prognozy
plt.legend()                     # Legenda do wykresu
plt.xlabel("Body weight")         # Oś X
plt.ylabel("Brain weight")        # Oś Y
plt.title("Predictions for New Animals")  # Tytuł wykresu
plt.show()                        # Wyświetlenie wykresu

# Wyświetlenie współczynników modelu
print("Współczynnik nachylenia (coef_):", lr.coef_)     # Ile zmienia się brain na każdy kg body
print("Wyraz wolny (intercept_):", lr.intercept_)       # Wartość brain, gdy body = 0
# Jeśli R² (test) jest zbliżone do R² (train) — model generalizuje dobrze.
# Jeśli R² (test) jest dużo gorsze od R² (train) — model może być przetrenowany (overfitting).
# Twój model dobrze dopasował się do danych treningowych – wyjaśnia aż 84% zmienności masy mózgu na podstawie masy ciała.
# 👉 To znaczy: model nauczył się zależności dla danych, które widział podczas treningu.
# ❌ R² (test) = -0.25 – zły wynik.
# Tu model się nie sprawdził na nowych danych. Negatywne R² oznacza, że model przewiduje gorzej niż prosta średnia 😬.