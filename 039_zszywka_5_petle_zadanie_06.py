# Zad. 6
# Zadanie polega na napisaniu programu, który będzie sumować liczby całkowite wpisane przez użytkownika tak długo,
# aż po wczytaniu poprzedniej liczby suma zwiększyła się. Na koniec program wypisuje ostateczną sumę Początkowo suma
# wynosi 0. Zastosuj do tego rozwiązania pętlę while.
# Przykład:
# Użytkownik przykładowo wprowadza kolejno liczby 1, 2, 3, 0 wtedy zwrócona suma to 1 + 2 + 3 + 0 = 6.
# Z kolei dla liczb 1, 9, 2, -12 suma wyniesie 0.



suma = 0
poprzednia_suma = -1

while suma != poprzednia_suma:
    liczba = int(input("Podaj liczbę całkowitą: "))
    poprzednia_suma = suma
    suma += liczba

print("Suma nie zwiększa się dalej. Wynosi: ", suma)