# Pytanie 13
# stwórz dwie listy:
# A - zawierającą liczby od 1 do 10
# B - zawierającą co trzecią liczbę z zakresu od 100 do 1
# w obu przypadkach możesz napisać tylko jedną linijkę kodu


# list_a = list(number for number in range(11))
# print(list_a)
print(list(number for number in range(1, 10, 3)))


print(list(number for number in range(11)))
# znak minus idziemy do dołu
print(list(number for number in range(100, 0, -3)))
