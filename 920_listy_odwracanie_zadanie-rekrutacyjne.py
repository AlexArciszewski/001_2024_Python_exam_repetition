# Pytanie 11 - na podstawie listy jezyki stworz listę jezyki_odwrocone
# zawierającą elementy listy jezyki w odwroconej kolejnosci

jezyki = ['Python', 'Java', 'C#', 'Ruby']

language_reversed_list = jezyki[::-1]
print(language_reversed_list)
# ['Ruby', 'C#', 'Java', 'Python']

jezyki2 = jezyki
jezyki2.reverse()
print(jezyki2)
# ['Ruby', 'C#', 'Java', 'Python']