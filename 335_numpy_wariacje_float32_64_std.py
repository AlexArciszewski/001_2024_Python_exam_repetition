import numpy as np

data = np.array([[10, 7, 4],
                 [ 3, 2, 1]])

#Wariancja dla całej tablicy
var_all = np.var(data)
print("Wariancja dla całej tablicy:", var_all)

#Wariancja dla każdej kolumny (axis=0)
var_columns = np.var(data, axis=0)
print("Wariancja dla każdej kolumny:", var_columns)

#Wariancja dla każdego wiersza (axis=1)
var_rows = np.var(data, axis=1)
print("Wariancja dla każdego wiersza:", var_rows)

#Odchylenie standardowe dla całej tablicy
std_all = np.std(data)
print("Odchylenie standardowe dla całej tablicy:", std_all)

#Dla każdej kolumny
std_columns = np.std(data, axis=0)
print("Odchylenie standardowe dla każdej kolumny:", std_columns)

#Dla każdego wiersza
std_rows = np.std(data, axis=1)
print("Odchylenie standardowe dla każdego wiersza:", std_rows)

#Duży rozmiar
data = np.zeros((2, 1000000))
data[0, :] = 1.0
data[1, :] = 0.1

print("Średnia (float32):", np.mean(data, dtype=np.float32))
print("Średnia (float64):", np.mean(data, dtype=np.float64))

#Mały rozmiar
data_small = np.zeros((2, 10))
data_small[0, :] = 1.0
data_small[1, :] = 0.1

print("Średnia dla małego zbioru (float32):", np.mean(data_small, dtype=np.float32))
print("Średnia dla małego zbioru (float64):", np.mean(data_small, dtype=np.float64))
    # float32 ma mniejszą precyzję niż float64, więc dla dużych zbiorów może gubić dokładność, zwłaszcza gdy wartości różnią się rzędem wielkości (jak 1.0 i 0.1).

    # Dla małych zbiorów float32 zwykle wystarcza – różnice są pomijalne.

    # float64 to podwójna precyzja, dlatego daje dokładniejsze wyniki kosztem wydajności.


