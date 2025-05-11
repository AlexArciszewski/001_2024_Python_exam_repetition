import numpy as np

data = np.array([[10, 7, 4],[3, 2, 1]])
print(data)

# wyznacz wartość średnią dla całej tablicy
print(data.mean())

#wyznacz wartość średnią dla każdej kolumny (skorzystaj z parametru axis=0)
print(data.mean(axis=0))

#wyznacz wartość średnią dla każdego wiersza (skorzystaj z parametru axis=1)
print(data.mean(axis=1))

#Średnia ważona (skorzystaj z funkcji average):
mean_all = np.average(data)
print(mean_all)
# Średnia ważona dla każdej kolumny (axis=0)
mean_columns = np.average(data, axis=0)
print("Średnia dla każdej kolumny:", mean_columns)

# Średnia ważona dla każdego wiersza (axis=1)
mean_rows = np.average(data, axis=1)
print("Średnia dla każdego wiersza:", mean_rows)

# Średnia ważona dla każdego wiersza z wagami [0, 1, 1]
weights1 = np.array([0, 1, 1])
mean_rows_weights1 = np.average(data, axis=1, weights=weights1)
print("Średnia ważona wierszy (wagi 0,1,1):", mean_rows_weights1)

#Średnia ważona dla każdego wiersza z wagami [2, 3, 5]
weights2 = np.array([2, 3, 5])
mean_rows_weights2 = np.average(data, axis=1, weights=weights2)
print("Średnia ważona wierszy (wagi 2,3,5):", mean_rows_weights2)
#Dla pierwszego wiersza: (2*10 + 3*7 + 5*4)/10 = (20 + 21 + 20)/10 = 61/10 = 6.1
#Dla drugiego: (2*3 + 3*2 + 5*1)/10 = (6 + 6 + 5)/10 = 17/10 = 1.7