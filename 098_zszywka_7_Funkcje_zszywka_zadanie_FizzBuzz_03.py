# Zad 3.
# Napisz funkcję fizz_buzz, która przyjmuje argument liczbowy.
# 1.	Jeżeli liczba jest podzielna przez 3, funkcja powinna zwrócić “Fizz”.
# 2.	Jeżeli liczba jest podzielna przez 5, zwróć “Buzz”.
# 3.	Jeżeli liczba jest podzielna równocześnie przez 3 i 5, zwróć “FizzBuzz”.
# 4.	W przeciwnym razie, zwracaj przekazaną liczbę.





def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number



print(fizz_buzz(5))