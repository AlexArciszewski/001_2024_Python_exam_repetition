# Zad2
# Program ma (w zadaniach zastosuj nowy sposób formatowania tekstu f-string):
# ●	zapytać ile kotów ma Ala i pobrać od użytkownika tę liczbę
# ●	wyświetlić na ekranie zdanie:  ‘Dzisiaj Ala znalazła jeszcze 3 koty …’
# (zamiast kropek napisz od siebie gdzie je znalazła)
# ●	dodać 3 do wprowadzonej wcześniej liczby
# ●	wyświetlić na ekranie zdanie:  ‘Teraz Ala ma już … kotów’ (w miejsce kropek wpisujecie obliczoną przez
#     program prawidłową liczbę)
# ●	wyświetlić to zdanie tak, aby każde słowo było oddzielone przecinkiem
# ●	wyświetlić to zdanie tak, by każde słowo znajdowało się w osobnej linijce
# ●	sprawdzić, czy wszystkie litery są małe i jeśli nie, to zamienić je na małe (wyświetl  wynik tej zmiany)
# ●	zmień pierwszą literę zdania na wielką i wyświetl zdanie po tej modyfikacji.

# zapytać ile kotów ma Ala i pobrać od użytkownika tę liczbę
print("Hello to Ala's cat calculator. ")
cats_number = int(input("How many cats does Ala have? "))

# wyświetlić na ekranie zdanie:  ‘Dzisiaj Ala znalazła jeszcze 3 koty …’
# (zamiast kropek napisz od siebie gdzie je znalazła)

total_catculator = cats_number + 3
print("Today she found ahother 3 cats in the woods")

# ●	wyświetlić na ekranie zdanie:  ‘Teraz Ala ma już … kotów’ (w miejsce kropek wpisujecie obliczoną przez
#     program prawidłową liczbę)
print(f"She has now {cats_number + 3} cats.")
sentence = "She has now " + str(total_catculator) + " cats."
print(sentence)
# She has now 5 cats.
splitted = sentence.split(" ")
print(splitted)
# ['She', 'has', 'now', '5', 'cats.']

# wyświetlić to zdanie tak, aby każde słowo było oddzielone przecinkiem
splitted_connected = ",".join(splitted)
print(splitted_connected)
# She,has,now,5,cats.

# wyświetlić to zdanie tak, by każde słowo znajdowało się w osobnej linijce
for word in splitted:
    print(word)

# She
# has
# now
# 15
# cats.

# sprawdzić, czy wszystkie litery są małe i jeśli nie, to zamienić je na małe (wyświetl  wynik tej zmiany)

print(sentence)
print(sentence.islower())
print(sentence.lower())
# zmień pierwszą literę zdania na wielką i wyświetl zdanie po tej modyfikacji.
print(sentence.capitalize())

