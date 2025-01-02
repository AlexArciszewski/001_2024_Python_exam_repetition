#Zadanie 1.Stwórz tablicę *ndarray* zawierającą liczby 3,9,1,3,5.

import numpy as np

x = np.array(([3, 9, 1, 3, 5]))
print(x)

#Zadanie 2.Stwórz tablicę *ndarray*, która będzie zawierała liczby od 1 do 50.

y = np.arange(1, 51)
print(y)

#Zadanie 3. Stwórz tablicę *ndarray*, która będzie zawierała 50 równoodległych punktów między
# liczbami 0 i 100.


z = np.linspace(0, 100, 50)
print(z)

#Zadanie 4. Stwórz tablicę *ndarray*, która będzie zawierała 100 równoodległych punktów między 0 i 100.

a = np.linspace(0,100,100)
print(a)

#Zadanie 5. Stwórz dwuwymiarową tablicę składającą się z liczb 1,2,3 i 4,5,6.

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)


#Zadanie 6. Stwórz tablicę 4x5, która zawiera same zera.

c = np.zeros((4, 5))
print(c)

#Zadanie 7. Stwórz tablicę 3x2, która zawiera same jedynki.
d = np.ones((3, 2))
print(d)


#Zadanie 8. Stwórz tablicę od zawierającą same parzyste liczby od 1 do 100.


my_list = [x for x in range(1, 101) if x % 2 == 0]
#print(my_list)
e = np.array(my_list)
print(e)

f = np.arange(2, 101, 2)
print(f)

#Zadanie 9. Stwórz tablicę o wymiarze 3x2 składającą się z liczb 1,2 i 2,3 i 3,4.

g = np.array([[1, 2], [2, 3], [3, 4]])
print(g)

















