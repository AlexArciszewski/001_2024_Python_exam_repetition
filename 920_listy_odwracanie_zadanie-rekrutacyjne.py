# Pytanie 11 - na podstawie listy jezyki stworz listę jezyki_odwrocone
# zawierającą elementy listy jezyki w odwroconej kolejnosci

# jezyki = ['Python', 'Java', 'C#', 'Ruby']
#  4 opcje rozwiązania

# A
jezyki = ['Python', 'Java', 'C#', 'Ruby']
language_reversed_list = jezyki[::-1]
print(language_reversed_list)
# ['Ruby', 'C#', 'Java', 'Python']

# B
jezyki2 = jezyki
jezyki2.reverse()
print(jezyki2)
# ['Ruby', 'C#', 'Java', 'Python']
# Metoda trwale nadpisuje liste

# C
jezyki = ['Python', 'Java', 'C#', 'Ruby']
jezyki3 = reversed(jezyki)
print(jezyki3)
# <list_reverseiterator object at 0x00000258432D5600>
jezyki = ['Python', 'Java', 'C#', 'Ruby']
# trzeba użyc list(reversed(list))
jezyki4 = list(reversed(jezyki))
print(jezyki4)
# ['Ruby', 'C#', 'Java', 'Python']

# D
jezyki = ['Python', 'Java', 'C#', 'Ruby']
jezyki5 = []
for jezyk in jezyki:
    jezyki5.insert(0, jezyk)
print(jezyki5)
# ['Ruby', 'C#', 'Java', 'Python']
# wyjaśnienie
# ['Python'] idzie na index 0
# ['Python'] 'Java' idzie na index 0
# ['Java', 'Python'] itd...