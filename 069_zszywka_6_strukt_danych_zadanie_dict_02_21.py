# Zad 2.
# Zmodyfikuj kod z zadania 1 tak, aby możliwe było dodawanie i usuwanie przez użytkownika informacji o
# nowych albumach do słownika. Program ma zawierać proste menu.
from typing import Callable


dict_of_albums = {
                    'The Sensual World' : 'Kate Bush',
                    'Shaday' : 'Ofra Haza',
                    'Achtung Baby' : 'U2',
                    'Aion' : 'Dead Can Dance',
                    'Invisible Touch' : 'Genesis'
                }

def menu():
    print("             MENU")
    print("1 Add album to the database")
    print("2 Remove album from the database")
    print("3 Check all the albums in the database")
    print("4 Find the album in the database")
    print("5 Exit the program")


def add_album():
    print("Adding new band  & album ...")
    album = input("Pls give me the name of the album U wanna add: ")
    band = input("Pls give me the name of the band U wanna add: ")
    dict_of_albums.update({album: band})
    print(f"The final result is {dict_of_albums}")
    menu()
def remove_album():
    album = input("Pls give me the name of the album U wanna delete: ")
    band = input("Pls give me the name of the band U wanna delete: ")
    if album in dict_of_albums.keys():
        del dict_of_albums[album]
        print(dict_of_albums)
        menu()


def check_albums():
    print(dict_of_albums)

def find_album():
    album = input("Pls give me the name of the album U wanna find: ")
    if album in dict_of_albums.keys():
        print(album, dict_of_albums[album])
        menu()

def exit_the_program():
     print("Bye")

def run_program():
    options: dict[int, Callable] ={
        1: add_album,
        2: remove_album,
        3: check_albums,
        4: find_album,
        5: exit_the_program
    }
    while True:
        menu()
        # dict_word()
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Exiting...")
            exit_the_program()
            break
        elif choice in options:
            options[choice]()
        else:
            print("Invalid choice. Please try again.")







if __name__ == "__main__":
    run_program()