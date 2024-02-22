# Zad 3.
# Napisz program, który poprosi użytkownika o podanie zestawu ulubionych przez niego kolorów (dowolna liczba).
# powinny być wpisane w jednej linii jako tekst i rozdzielone spacją.
# W programie powinien znajdować się zbiór Twoich ulubionych kolorów. Należy porównać oba zbiory:
# Twój i użytkownika oraz sprawdzić, czy są jednakowe. Jeśli tak, należy wydrukować odpowiedni komentarz,
# jeśli nie należy podać te kolory, które:
# ●	wybrały obie osoby
# ●	wybrał tylko użytkownik
# ●	preferuje jedynie autor programu


# color = input("Pls write some colors: ")
colors = "czerwony zolty zielony niebieski bialy czarny brazowy rozowy srebrny zloty"
# colors = "czerwony niebieski czarny"
list_colors = colors.split(" ")
print(list_colors)

set_user_colors = set(list_colors)
print(set_user_colors)


my_colors = ["czerwony", "niebieski", "czarny", "camelowy"]
set_my_colors = set(my_colors)
print(set_my_colors)


if set_user_colors == set_my_colors:
    print("True")
else:
    print("Sets are different")

print("user chose: ")
for color in list_colors:
    print(color)

print("My colors were: ")
[print(col) for col in my_colors]

print("our colors were: ")
print(set_user_colors & set_my_colors)
print("colors chosen only by user: ")
print( set_user_colors - set_my_colors)

print("colors chosen only by admin: ")
print(set_my_colors - set_user_colors)
