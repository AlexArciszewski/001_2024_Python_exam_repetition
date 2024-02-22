# Zad 6.
# 1. Użytkownik wybiera czy obstawia reszkę, czy orła (literka r – reszka,
# literka o – orzeł)
# 2. Po dokonaniu wyboru, Komputer odlicza 3,2,1, a następnie dokonuje
# 'rzutu', czyli losowego wyboru orzeł / reszka.
# 3. Komputer wyświetla wynik rzutu.
# 4. Jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli
# komputer to dodaje punkt dla komputera.
#
# Podpowiedź:
# W celu losowania wartości wykorzystaj metodę randint() (pamiętaj o linijce import random na samej
# górze programu) i przypisz konkretne liczby do orła/reszki.


import random


player_points = 0
computer_points = 0
heads_tails = input("Choose heads or tails: ")
for i in range(1, 4):
    print(i)

coin = ["heads", "tails"]
computer_choice = random.choice(coin)
print(computer_choice)
if computer_choice == heads_tails:
    player_points += 1
    print("player won")
else:
    print("player loses")
    computer_points += 1
print(f"The score is computer {computer_points}, player {player_points}")



