# Zad 7.
# Wykorzystując instrukcje warunkowe, stwórz funkcjonalność wyliczania wartości bezwzględnej z podanej przez użytkownika
# liczby, np. -5 zamieniane na 5, 5 bez zmian, czyli pozostaje 5.
# Wartością bezwzględną dowolnej liczby rzeczywistej x to:
# ●	ta sama liczba rzeczywista x, gdy podane x ≥ 0
# ●	liczba −x (przeciwna do x), gdy podane x < 0

number = int(input("?"))
print(f"The result is {abs(number)}")