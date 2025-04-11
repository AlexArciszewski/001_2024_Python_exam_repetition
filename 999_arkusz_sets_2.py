# Napisz program, który poprosi użytkownika o podanie zestawu ulubionych przez niego kolorów (dowolna liczba). Kolory powinny być wpisane w jednej linii jako tekst i rozdzielone spacją.
# W programie powinien znajdować się zbiór Twoich ulubionych kolorów. Należy porównać oba zbiory:
# Twój i użytkownika oraz sprawdzić, czy są jednakowe. Jeśli tak, należy wydrukować odpowiedni komentarz, jeśli nie należy podać te kolory, które:
# ●	wybrały obie osoby
# ●	wybrał tylko użytkownik
# ●	preferuje jedynie autor programu
from typing import Callable, Dict


def main() -> None:
    user_set = set()
    color_set = {"czerwony"}

    def menu() -> None:
        print("\nChoose options:")
        print("1 - Menu")
        print("2 - Add to color set")
        print("3 - Delete from set")
        print("4 - Exit")
        print("5 - Check colors")

    def check_set() -> None:
        print(color_set)
        print(user_set)

        if color_set == user_set:
            print("sets are the same")
        else:
            print("sets are different")


    def add_to_set() -> None:
        color =input("color: ")
        user_set.add(color)


    def remove_from_set() -> None:
        print(user_set)
        rem_set = input("pls give me the color U wanna delete: ")
        user_set.discard(rem_set)
        print(user_set)


    def exit_program() -> None:
        print('Exit...')
        exit()

    options: Dict[int, Callable[[], None]] = {
        1: menu,
        2: add_to_set,
        3: remove_from_set,
        4: exit_program,
        5: check_set,
    }

    while True:
        menu()
        try:
            user_choice = int(input("Choose your option: "))
        except ValueError:
            print("You have to give me the number.." )
            continue

        if user_choice in options:
            options[user_choice]()
        else:
            print("incorrect number")


if __name__ == "__main__":
    main()

