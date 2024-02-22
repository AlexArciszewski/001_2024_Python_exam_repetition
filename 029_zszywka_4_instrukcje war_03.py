# Zad 3.
# Pobierz od użytkownika 3 liczby i wyświetl największą z nich.

a = int(input("Input the a which is the first number: "))
b = int(input("Input the b which is the second number: "))
c = int(input("Input the c which is the third number: "))

if a > b and a > c:
    print(f"The winner is a={a}")
elif b > a and b > c:
    print(f"The winner is b={b}")
elif c > a and c > b:
    print(f"The winner is c={c}")
else:
    print("something went wrong")

