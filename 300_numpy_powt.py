#Powtórzenie wiadomości o numpy

#1. Załaduj moduł numpy
import numpy as np

print('zad.2\n')
#2. Utwórz w zmiennej a jednowymiarową tablicę z elementami od 0 do 19.
# Hint: Służy do tego metoda np.arange(...)

a = np.arange(20)
print(a)

#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print('zad.3\n')
#3. Wyświetl kształt tej tablicy. Hint: służy do tego właściwość shape

print(a.shape)
#(20,)
print('zad.4\n')
#4. Wyświetl zerowy element tablicy. Wyświetl czwarty element tablicy. Hint: Korzystaj z [] i numeruj od 0

print(a[0])
print(a[4])
#0
#4
print('zad.5\n')
#5. Zmień kształt tablicy na 2x10. Wynik przekształcenia zapisz w a. Potem ponownie sprawdź kształt i wyświetl zawartość tablicy.
# Hint: Skorzystaj z metody reshape(...)

a = a.reshape(2, 10)
print(a)
#[[ 0  1  2  3  4  5  6  7  8  9]
# [10 11 12 13 14 15 16 17 18 19]]

print('zad.6\n')
#6.  Wyświetl element zerowy z przekształconej w poprzednim kroku tablicy. Czy jest to ten sam element co poprzednio?
print(a[0])
#[0 1 2 3 4 5 6 7 8 9]

print('zad.7\n')
#7. (Uwaga - tu będzie błąd, ale na błędach człowiek się uczy, więc to dobrze). Wyświetl czwarty element z tablicy a
#print(a[4])
print(len(a))
#2 są dwa elementy po reshape nie 20 i nie 4

print('zad.8\n')
#8. A teraz zróbmy to poprawnie. Z tablicy a wyświetl czwarty element znajdujący się w zerowym wierszu.
# Hint: Musisz dwa razy skorzystać z [][]

print(a[0][4])
#4

print('zad.9\n')
#9. Zmień kształt tablicy a na 2x5x2

a = a.reshape(2, 5, 2)
print(a)

#[[[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]]

#[[10 11]
#  [12 13]
#  [14 15]
#  [16 17]
#  [18 19]]]

print('zad.10\n')
#10. Potem ponownie sprawdź kształt i wyświetl zawartość tablicy. Hint: hahah - poszukaj odpowiedniego hinta powyżej :)

print(a.shape)

#(2, 5, 2)

print('zad.11\n')
#11. Wyświetl z tablicy a:
#
#    zerowy wiersz
#
#    czwartą kolumnę z zerowego wiersza
#
#    drugi element z czwartego wiersza w zerowym wierszu

print(a[0])
print(a[0][4])
print(a[0][4][1])

#[[0 1]
# [2 3]
# [4 5]
# [6 7]
# [8 9]]

#[8 9]

#9


print('zad.12\n')
#12. Tworząc tablicę, możesz od razu definiować jej kształt. Utwórz tablicę b korzystając z parametrów przekazywanych do metody array
# lub wywołując odpowiednie metody
# dla już istniejącej tablicy, tak aby zawierała ona elementy parzyste od 0 do 40 o kształcie 4x5


even_numbers = np.arange(0, 40, 2)
b = even_numbers.reshape(4, 5)
print(b)

#[[ 0  2  4  6  8]
# [10 12 14 16 18]
# [20 22 24 26 28]
# [30 32 34 36 38]]


print('zad.13\n')
#13. Polecenie
#a_python_list =  [2**x for x in range(10)]
#tworzy standardową pythonową listę dziesięciu kolejnych potęg dwójki. W oparciu o tą listę utwórz obiekt array c

a_python_list = [2**x for x in range(10)]
print(a_python_list)

c = np.array(a_python_list)
print(c)

#[  1   2   4   8  16  32  64 128 256 512]

print('zad.14\n')
#14. To może się wydawać trochę dziwne, ale czasami w uczeniu maszynowym potrzebne są bardzo specyficzne obiekty array.
# W tym zadaniu utworzysz takie "dziwaczne" tablice

#Utwórz tablicę zero_array składającą się z 10 zer. Hint: Skorzystaj z metody zeros
a = np.zeros((1, 10))
print(a)

#[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]


#Utwórz tablicę one_array składającą się z 10 jedynek. Hint: Skorzystaj z metody ones
a = np.ones((1, 10))
print(a)
#[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]

#Utwórz tablicę empty_array składającą się ze 100  byle-jakich-liczb. Hint skorzystaj z metody empty
#Ta metoda tworzy tablicę, która zawiera to, co akurat było w pamięci. Wielokrotne uruchamianie w/w
#polecenia może dawać różne wyniki, ale to nie jest jakiś świetny sposób na generowanie liczb losowych

b = np.empty((1, 100))
print(b)

#[[1.10286107e-311 1.10278839e-311 1.10278802e-311 1.10278433e-311
# 1.10278839e-311 1.10278839e-311 1.10278839e-311 1.10278832e-311
# 1.10278801e-311 1.10278424e-311 1.10278832e-311 1.10278839e-311
# 1.10278839e-311 1.10278313e-311 1.10278843e-311 1.10286107e-311
# 1.10278297e-311 1.10278795e-311 1.10278801e-311 6.95251362e-310
# 1.10286107e-311 1.10278843e-311 1.10278297e-311 1.10278795e-311
# 1.10278839e-311 1.10278839e-311 1.10278427e-311 6.95251362e-310
# 1.10278839e-311 1.10278832e-311 1.10278801e-311 1.10278801e-311
# 1.10278585e-311 1.10278839e-311 1.10278839e-311 6.95251362e-310
# 6.95251363e-310 1.10278832e-311 1.10278839e-311 1.10286088e-311
# 1.10286105e-311 6.95251368e-310 6.95251368e-310 6.95251368e-310
# 6.95251369e-310 6.95251368e-310 1.10286108e-311 1.10286106e-311
# 6.95251368e-310 6.95251368e-310 6.95251368e-310 1.10286088e-311
# 6.95251361e-310 6.95251368e-310 6.95251362e-310 1.10278832e-311
# 1.10286105e-311 1.10285574e-311 6.95251368e-310 6.95251363e-310
# 6.95251363e-310 1.10278313e-311 1.10278582e-311 6.95251368e-310
# 1.10286107e-311 1.10278450e-311 1.10286107e-311 1.10286107e-311
# 1.10286107e-311 1.10286106e-311 6.95251363e-310 6.95251368e-310
# 1.10278582e-311 1.10286105e-311 1.10286107e-311 1.10286045e-311
# 6.95251368e-310 1.10286107e-311 1.10286107e-311 6.95251368e-310
# 6.95251361e-310 6.95251362e-310 6.95251362e-310 6.95251363e-310
# 6.95251368e-310 6.95251363e-310 6.95251369e-310 6.95251368e-310
# 6.95251368e-310 6.95251368e-310 6.95251368e-310 6.95251368e-310
# 6.95251368e-310 6.95251362e-310 6.95251363e-310 6.95251362e-310
# 1.10278620e-311 1.10278330e-311 6.95251362e-310 1.10285445e-311]]


#Utwórz tablicę lucky_array o wymiarach 5x5 składającą się z samych trzynastek. Hint: Skorzystaj z metody full

lucky_array = np.full((5, 5), 13)
print(lucky_array)

#[[13 13 13 13 13]
# [13 13 13 13 13]
# [13 13 13 13 13]
# [13 13 13 13 13]
# [13 13 13 13 13]]

#Utwórz tablicę diagonal_array o wymiarach 5x5, która na przekątnej ma jedynki, a pozostałe wartości to zera.
# Hint: Skorzystaj z metody eye


diagonal_array = np.eye(5)
print(diagonal_array)

#[[1. 0. 0. 0. 0.]
# [0. 1. 0. 0. 0.]
# [0. 0. 1. 0. 0.]
# [0. 0. 0. 1. 0.]
#[0. 0. 0. 0. 1.]]


#Utwórz tablicę random_array składającą się z 10 losowych liczb. Hint: Skorzystaj z metody np.random.random


random_array = np.random.random((10))
print(random_array)


#[0.9847564  0.38474891 0.74583053 0.77265686 0.34812263 0.69649965
# 0.7082748  0.08857743 0.08545177 0.51897346]

#Utwórz tablicę linspace_array zawierającą 5 elementów, która jako zerową wartość ma 100, jako ostatnią ma wartość
# 200, i wszystkie elementy różnią się od siebie o tyle samo. Hint: Skorzystaj z metody linspace

linspace_array = np.linspace(100, 200, 5)
print(linspace_array)

#[100. 125. 150. 175. 200.]




