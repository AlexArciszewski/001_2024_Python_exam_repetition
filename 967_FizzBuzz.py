# Pytanie 39 - napisz program, który dla kolejnych liczb z zakresu od 1 do n:
# wypisze: "Fizz" - jeśli liczba będzie podzielna przez 3
# wypisze: "Buzz" - jeśli liczba będzie podzielna przez 5
# wypisze: "FizzBuzz" - jeśli liczba będzie podzielna przez 3 i 5
# jeśli nie zajdzie żaden z tych przypadków, to wypisz po prostu liczbę.
# Zadanie to znane jest pod nazwą: FizzBuzz.

from typing import Union


def fizz_buzz(number: int) -> Union[int, str]:
    """FizzBuzz number checker"""

    for number in range(1, number + 1):
        if number % 3 == 0 and number % 5 == 0:
            print(f"FizzBuzz")
        if number % 3 == 0 and number % 5 != 0:
            print("Fizz")
        if number % 5 == 0 and number % 3 != 0:
            print("Buzz")
        if number % 5 != 0 and number % 3 != 0:
            print(number)


fizz_buzz(16)

print("\n Opcja nr 2 \n")


def fizzbuzz2(n):
    for num in range(1, n+1):
        wynik = ''              # w każdym obiegu pętli tworzymy pusty string do przechowywania wyniku
        if num % 3 == 0:
            wynik += "Fizz"     # wynik = wynik + "Fizz"
        if num % 5 == 0:
            wynik += "Buzz"
        if num % 3 != 0 and num % 5 != 0:
            wynik = str(num)    # jeśli liczba nie jest podzielna ani przez 3 ani przez 5
        print(wynik)            # to do zmiennej wynik dodajemy stringa utworzonego z tej liczby


fizzbuzz2(15)