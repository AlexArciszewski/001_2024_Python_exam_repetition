#Zadanie 1. Stwórz dwie tablice, jedna składająca się z liczb 1,2,3 i druga składająca się z liczb 4,4,4.

import numpy as np


a = np.array([1, 2, 3])

b = np.array([4, 4, 4])

print(a, b)


#Zadanie 2. Dodaj do siebie tablice a i b. Wydrukuj wynik.

c = a + b
print(c)

#Zadanie 3. Odejmij od siebie tablice a i b. Wydrukuj wynik.

d = a - b
print(d)


#Zadanie 4. Pomnóż przez siebie tablice a i b. Wydrukuj wynik.

#mnożenie elemntów przez siebie nie tak jak w macierzach
e = a * b
print(e)

#mnozenie matematyczne
#Mnozenie matematyczne funkcja np.matmul w drugim wierszy co w pierwszym kolumn musi być
#to da bląd
#print(np.matmul(a, b))

#f = np.matmul(a, b)
#print(f)

#Zadanie 5. Podziel tablicę a przez b. Wydrukuj wynik.

f = a/b
print(f)


#Zadanie 6. Wykonaj transpozycję sumy tablic a i b. Tablicę wynikową zapisz do zmiennej d. Wydrukuj wynik.

a = np.array([1, 2, 3])

b = np.array([4, 4, 4])

print(d)
e = (a+b).T
print(e)


#Zadanie 7. Sprawdź, które elementy tablicy e sa większe od 5.

e = (a+b).T
print(e>5)

#Zadanie 8. Sprawdź rozmiar tablicy e.

print(np.size(e))