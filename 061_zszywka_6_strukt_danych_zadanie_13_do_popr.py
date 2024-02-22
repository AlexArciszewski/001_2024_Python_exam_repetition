# Zad 13.
# Utwórz słownik, który przechowuje definicje wyrazów i ich wytłumaczenia.
# Zarządzanie słownikiem ma się odbywać za pomocą interaktywnego
# MENU (MENU ma być obsługiwane za pomocą print() oraz input() oraz ma wyglądać tak jak poniżej):
# 1. Dodaj słowo wraz z definicją
# 2. Znajdź definicję słowa
# 3. Usuń słowo wraz z definicją z słownika
# 4. Zakończ program
#

from typing import Callable

dict_words = {}


def menu():
    'menu option'
    print("Menu")
    print("1. Add word to a dict: ")
    print("2. Remove word from the dict: ")
    print("3. Find a word in the dict: ")
    print("4. Show dict status: ")
    print("5. Exit")



def show_dict_status():
    print(dict_words)

def add_word_to_dict():
    'method used to add a word to a dict'
    print("Adding word to a dict")
    word = input(f"Pls input the word")
    meaning = input(f"Please input the meaning of the {word} given")
    new_item = {word : meaning}
    dict_words.update(new_item)
    print(dict_words)

def remove_from_the_dict():
    'method used to remove the word'
    print("Removing word from the dict")


def find_word_in_dict():
    'method used to find a word'
    print("Finding the word")


def run_program():
    "method used for starting the program"
    options: dict[int, Callable] = {
        1: add_word_to_dict,
        2: remove_from_the_dict,
        3: find_word_in_dict,
        4: show_dict_status
    }
# #UWaga!!
#     1: add_word_to_dict(),
#     2: remove_from_the_dict(),
#     3: find_word_in_dict()
# Nie wolno tak robić! tworze funkcje a nie liste funkjci.....


    while True:
        menu()
        # dict_word()
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Exiting...")
            break
        elif choice in options:
            options[choice]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    run_program()