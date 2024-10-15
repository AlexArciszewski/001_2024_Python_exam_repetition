# map() stosuje funkcję do elementów sekwencji i zwraca przekształconą listę.
# zip() łączy elementy z dwóch lub więcej sekwencji w pary (lub krotki).
# Map prykład z użyciem listy
# Załóżmy, że mamy listę liczb, a chcemy uzyskać ich kwadraty za pomocą map().
numbers = []
for i in range(41):
    numbers.append(i)
print(numbers)


def square(x: int) -> int:
    """Function used to square the numbers"""

    return x**2

print("Map i kwadraty liczb")
squared_numbers = list(map(square, numbers))
print(squared_numbers)

# dostajemy:<map object at 0x0000029218B8BE20> bez wpisania list
# iterator zmieniamy na listę
print(list(squared_numbers))


# Zip
# zip() łączy elementy z wielu iterowalnych obiektów w krotki. Zwraca obiekt zip, który można przekonwertować np. na listę krotek.
# Jeśli jedna z list jest dłuższa, zip() zatrzyma się po zakończeniu najkrótszej listy.
# Przykład:
# Załóżmy, że mamy dwie listy: jedną z imionami i drugą z wiekiem. Chcemy je sparować za pomocą zip().

print("zip")
names = ["Anna", "Barbara", "Jan"]
ages = [25, 30, 22]

# Lączyy wiek i osoby

paired = list(zip(names, ages))
print(paired)
# /dostajemy iterator zmieniamy na lsitę bo dostaliśmy <zip object at 0x0000021E66BC73C0>

print(list(paired))
# [('Anna', 25), ('Barbara', 30), ('Jan', 22)]


print("MAP +ZIP")

# Listy długości
meters = [1, 2, 3]
centimeters = [50, 25, 75]

# Użycie zip() do sparowania odpowiadających sobie długości
paired = zip(meters, centimeters)

# Użycie map() z funkcją lambda do dodania długości w metrach i centymetrach
# Dla każdej krotki x (gdzie x[0] to długość w metrach, a x[1] to długość w centymetrach), oblicza całkowitą długość w centymetrach, używając funkcji lambda.
total_lengths = map(lambda x: x[0] * 100 + x[1], paired)

# Konwersja wyniku na listę i wyświetlenie
print(list(total_lengths))
# [150, 225, 375]








