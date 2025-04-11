music_dict = {'The Sensual World' : 'Kate Bush',
              'Shaday' : 'Ofra Haza',
              'Achtung Baby' : 'U2',
              'Aion' : 'Dead Can Dance',
              'Invisible Touch' : 'Genesis'
              }

print(music_dict.keys())

for keys in music_dict.keys():
    print(keys)

music_dict_key = input("Pls input Checking the key: ")

if music_dict_key in music_dict.keys():
    print(f"Wykonawcą albumu {music_dict_key} jest{music_dict[music_dict_key]}")
else:
    print("nie ma takiego albumu")



from typing import Callable

options: dict[int, Callable] = {
    1: menu,
    2: add_to_list,
    3: remove_from_list,

}

user_choice = int(input("Podaj swój wybór: "))



