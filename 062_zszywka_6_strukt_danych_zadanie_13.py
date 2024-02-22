# Zad 13.
# Utwórz słownik, który przechowuje definicje wyrazów i ich wytłumaczenia.
# Zarządzanie słownikiem ma się odbywać za pomocą interaktywnego
# MENU (MENU ma być obsługiwane za pomocą print() oraz input() oraz ma wyglądać tak jak poniżej):
# 1. Dodaj słowo wraz z definicją
# 2. Znajdź definicję słowa
# 3. Usuń słowo wraz z definicją z słownika
# 4. Zakończ program
#
import sys
start_message = """ Choose option     
    1. Add a word along with its definition
    2. Find the definition of a word
    3. Remove a word along with its definition from the dictionary
    4. End the program   """

program_running = True
if program_running == False:
    sys.exit(1)





while program_running == True:
    number = int(input(f"hello, {start_message} "))
    if number == 1:
        dict_words = {}
        a = input("pls give me the word: ")
        b = input(f"pls give me the meaning of {a} word: ")
        c = {a : b}
        dict_words.update(c)
        print(c)
    elif number == 2:
        y = input("Find the word u wanna check: ")
        for key in dict_words.keys():
            if key == y:
                print(dict_words[key])

    elif number == 3:
        z = input("Pls give me the word U wanna delete; ")
        # for key in dict_words.keys():     to źle bonie można usuwac el ze słownika po którym się iteruje
        #     if key == z:
        if z in dict_words.keys():
            dict_words.pop(z)
        print(f"word was successfully deleted")
        print(dict_words)

        pass
    elif number == 4:
        print("program will now exit....")
        program_running = False
        pass
    else:
        print(f"Something went wrong")