print("Tuple")
#  wyśeietlenie danych z tupli

names_list11 = ("Celina", "Dorota","Adam", "Barbara", "Ewa","Karol")
print(names_list11)

for names in names_list11:
    print(names)


# ity element
print(names_list11[0])

#długość tupli
person = ("Aleksander", "Arciszewski", 39)
print(person)

#zliczanie el. w tupli
print(len(person))

# zwrócenie nr konkretnego el
print(person.count("Aleksander"))


person = ('robert', 'junior')

name, surname = person

name, surname = person[0], person[1]

name = person[0]
surname = person[1]