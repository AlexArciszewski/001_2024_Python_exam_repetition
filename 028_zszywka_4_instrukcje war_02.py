# Zad 2.
# Napisz program sprawdzający, czy podana przez użytkownika jest ujemna, dodatnia lub czy ma wartość
# równą 0.

number = int(input("Pls give me the number: "))
if number < 0:
    print("negative number")
elif number > 0:
    print("positive number")
elif number == 0:
    print("0")
else:
    print("something went wrong")

