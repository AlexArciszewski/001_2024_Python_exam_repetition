# Zad 10.
# Zgadnij liczbę.
# To chyba jedno z najpopularniejszych wyzwań, z którymi mogą się zmierzyć kadeci programowania, aby jeszcze lepiej
# poznać pętle i instrukcje warunkowe.
# Program ma realizować pobranie od użytkownika przedziału (dolnego i górnego) liczb i następnie ma wylosować wartość z
# podanego przedziału. Następnie realizowana jest już główna część programu – czyli użytkownik ma odgadnąć wylosowaną
# liczbę. Proces wygląda tak, że użytkownik podaje liczbę, program sprawdza, czy jest to wylosowana wcześniej
# liczba - jeśli nie, to podaje informacje, czy użytkownik podał za dużą czy małą liczbę i daje mu możliwość ponownego
# wpisania wartości. Po każdej błędnej próbie, użytkownikowi nalicza się 1 ujemny punktów (zaczyna od ilości punktów
# równej różnicy przedział_górny - przedział_dolny). Po odgadnięciu liczby, na ekranie powinien wyświetlać się komunikat
# “Gratulacje! Zdobyłeś X punktów” (X - wartość punktacji użytkownika).

import random
import sys
shots = 0
game_is_on = True
if game_is_on == False:
    sys.exit(1)


lower_number = int(input("Give me the lower number: "))
upper_number = int(input("Give me the upper number: "))
print(f"Number will be chosen for the range between the {lower_number} and the {upper_number}")

x = random.randint(lower_number, upper_number + 1)
while game_is_on == True:
    tried_number = int(input("Give your best shot: "))

    if tried_number == x:
        shots += 1
        print("congratulation, U won ")
        print(f"U used {shots} chance(s)")
        game_is_on = False
    elif tried_number > x:
        shots += 1
        print(f"U used {shots} chance(s)")
        print("The number you chose is to high")
    elif tried_number < x:
        shots += 1
        print(f"U used {shots} chance(s)")
        print('The number U chose is to low')
    else:
        print("Something went wrong")



