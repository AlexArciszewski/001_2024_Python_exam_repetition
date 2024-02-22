# Zasymuluj grę w papier, kamień, nożyce. Oczywiście będzie to uproszczona wersja, ponieważ
# będzie zapewniała wprowadzenie danych tylko jednorazowo. Pobierz od użytkownika numer
# 1 słowo spośród: "kamień", "papier", "nożyce", operację przeprowadź również dla użytkownika numer 2.
# Następnie wyświetl, który z użytkowników wygrał to jednorazowe starcie (pamiętaj o tym,
# który przedmiot jest w grze "silniejszy" od drugiego). Dodatkowo zabezpiecz program przed wprowadzeniem
# nieprawidłowych danych, czyli jeżeli użytkownik nie wprowadzi ani "kamień", ani "papier", ani "nożyce"
# program ma natychmiastowo przerwać działanie i wyświetlić komunikat: "Błędne dane!".

#moja wersja :)

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to my paper,rock,scissors game")

option_list = ["paper", "rock", "scissors"]


your_choice = input("What do is your choice? Write: paper,rock,scissors. ")
computer_choice = random.choice(option_list)
print(f"Computer chose {computer_choice}")

if your_choice == "paper" and computer_choice == "rock":
    print("You won")
elif your_choice == "paper" and computer_choice == "scissors":
    print("You loose")
elif your_choice == "paper" and computer_choice == "paper":
    print("it's a draw")
elif your_choice == "rock" and computer_choice == "rock":
    print("it's a draw")
elif your_choice == "rock" and computer_choice == "scissors":
    print("You won")
elif your_choice == "rock" and computer_choice == "paper":
    print("You loose")
elif your_choice == "scissors" and computer_choice == "rock":
    print("You lost")
elif your_choice == "scissors" and computer_choice == "scissors":
    print("it's a draw")
elif your_choice == "scissors" and computer_choice == "paper":
    print("You win")
else:
    print("Something went wrong")