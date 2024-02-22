# Zad 5.
# Napisz program pobierający od użytkownika 2 liczby. Sprawdź, czy co najmniej 1 z nich jest parzysta.


number = int(input("pls give me the number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is not even")