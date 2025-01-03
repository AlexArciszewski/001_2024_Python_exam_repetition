
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

