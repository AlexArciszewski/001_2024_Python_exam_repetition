# Zad 4.
# Napisz program, który poprosi użytkownika o podanie imion kilku swoich dobrych znajomych.
# Korzystając z wprowadzonych danych, dla każdego z podanych znajomych, program ma wyświetlić
# spersonalizowany komunikat, na przykład powitanie, pozdrowienie, który będzie skierowany do konkretnej osoby.


some_names = input("names pls with , a separator: ")
# Ada, Ola, Dominika
some_names = some_names.replace(",", "")
some_list_names = some_names.split(" ")
# print(some_list_names)
for i in range(len(some_list_names)):
    print(f"Hello {some_list_names[i]}")
    if some_list_names[i] == "Ola":
        print(f"{some_list_names[i]} Give my money back ")
        i+=1

# Hello Ada
# Hello Ola
# Ola Give my money back
# Hello Dominika