#Tworzenie tablic wielowymiarowych
# np.array() wymaga podania konkretnych wartości
# np.arange() zwraca liczby z podanego przedziału co dany krok
# np.linspace() zwraca rowno rozłożone liczby w podanym przedziale

import numpy as np

#np.array
#pierwsza tablica jednowymiarowa
x = np.array([1, 2, 3, 4, 5])
print(x)
#[1 2 3 4 5]

# druga tablica 3 wymiary
y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(y)
#[[1 2 3]
# [4 5 6]
# [7 8 9]]

#np arange z pewnego rpzedzialuwybieramy wartosci

z = np.arange(5)
print(z)
#[0 1 2 3 4]

#sposob nr dwa argumenty poczatek i koniec przedzialu


w = np.arange(1, 11)
print(w)
#[ 1  2  3  4  5  6  7  8  9 10

#sposób nr trzy 2 argumenty i krok
w = np.arange(1, 11, 2)
print(w)
#[1 3 5 7 9]


#np.linespace zwraca róznorozmieszczone elementy z pewnego rpzedziału który podamy trzeci element to liczba elementów

c = np.linspace(0, 100, 5)
print(c)
#[  0.  25.  50.  75. 100.]

c = np.linspace(0, 100)
print(c)
#[  0.           2.04081633   4.08163265   6.12244898   8.16326531
#  10.20408163  12.24489796  14.28571429  16.32653061  18.36734694
#  20.40816327  22.44897959  24.48979592  26.53061224  28.57142857
#  30.6122449   32.65306122  34.69387755  36.73469388  38.7755102
#  40.81632653  42.85714286  44.89795918  46.93877551  48.97959184
#  51.02040816  53.06122449  55.10204082  57.14285714  59.18367347
#  61.2244898   63.26530612  65.30612245  67.34693878  69.3877551
#  71.42857143  73.46938776  75.51020408  77.55102041  79.59183673
#  81.63265306  83.67346939  85.71428571  87.75510204  89.79591837
#  91.83673469  93.87755102  95.91836735  97.95918367 100.  ]
print(len(c))
#50 elementów równo rozłozonych od 0 do 100