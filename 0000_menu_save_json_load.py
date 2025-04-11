from typing import Callable, Dict

import json


def main() -> None:
    global music_dict

    def menu() -> None:
        """Shows the menu."""
        print("Menu")

    def collection() -> None:
        """Displays the collection of albums and authors."""
        for album, author in music_dict.items():
            print(f"{album} - {author}")


    def add_to_list() -> None:
        """Adds a new album and author to the music dictionary."""
        album_name = input('Please give me the title of the album: ')
        author = input('Please give me the name of the author: ')
        new_data = {album_name : author }
        music_dict.update(new_data)
        print("Added to menu_dict")

    def remove_from_list() -> None:
        """Removes an album from the music dictionary."""
        album_name = input('Please give me the title of the album: ')
        print(f"You want to delete:{album_name}, {music_dict[album_name]}")
        music_dict.pop(album_name)
        print("Removed from menu_dict")

    def exit_program() -> None:
        """Exits the program."""
        print("Program will now exit")
        exit()

    def save_data() -> None:
        """Saves the music dictionary to a JSON file."""
        filename = input("Enter filename to save (e.g. music.json): ")
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(music_dict, f, indent=4)
            print(f"Saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

    def load_data() -> None:
        """Loads the music dictionary from a JSON file."""
        global music_dict
        filename = input("Enter the filename to load (e.g. music.json): ")

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                music_dict = json.load(f)
            print(f"Data loaded from {filename}")
        except FileNotFoundError:

            full_path = "C:\\Dane\\2_Python powt_cale\\001_python_rep_full\\" + filename
            print(f"File not found in current directory. Attempting to load from: {full_path}")

            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    music_dict = json.load(f)
                print(f"Data loaded from {full_path}")
            except FileNotFoundError:
                print(f"Error: The file was not found in either location.")
            except json.JSONDecodeError:
                print(f"Error: Failed to decode JSON.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


    music_dict = {'The Sensual World': 'Kate Bush',
                   'Shaday' : 'Ofra Haza',
                   'Achtung Baby' : 'U2',
                   'Aion' : 'Dead Can Dance',
                   'Invisible Touch' : 'Genesis'
                   }

    print(music_dict)
    #słownik mapuje liczby całkowite (opcje menu) do funkcji, które nie przyjmują argumentów i nie zwracają wartości.
    options: Dict[int, Callable[[], None]] = {
         1: menu,
         2: add_to_list,
         3: remove_from_list,
         4: exit_program,
         5: collection,
         6: save_data,
         7: load_data,
    }

    while True:
        print("\nChoose options:")
        print("1 - Menu")
        print("2 - Add to music_dict.")
        print("3 - Delete from the music_dict")
        print("4 - Exit")
        print("5 - Collection")
        print("6 - Save data to a file")
        print("7 - Load data from a file")

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









