# Zad1
# Program ma wykonać kilka operacji na pobranym od użytkownika dowolnym tekście (stringu),  który ma co najmniej
# siedem znaków. Operacje te to:
#   ●	wprowadzenie i wyświetlenie na ekranie tego tekstu
#   ●	wyświetlenie liczby znaków, które on zawiera
#   ●	wyświetlenie pierwszego i ostatniego znaku tego tekstu
#   ●	wyświetlenie dowolnych 3 znaków z środka tego tekstu.
import random

some_string = input("Please give me some text with minimum 7 letters: ")
word_box = []
random_box = []
if len(some_string) >=7:
    print(f" Chosen word is{some_string}")
    print(f" Chosen string has {len(some_string)}  words")
    print(f" The first and the last letters are: {some_string[0]} and {some_string[-1]}")
    for letter in some_string:
        word_box.append(letter)

    for _ in range(3):
        selected_word = random.choice(some_string)
        random_box.append(selected_word)
    print(f"Random letters are:{random_box}")



else:
    print("Pls Check your string(s) hyhy")
