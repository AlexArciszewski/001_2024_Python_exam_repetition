import random

fruits = ["apple", "banana", "cherry", "mango"]
random_fruit = random.choice(fruits)

print("Wylosowany owoc:", random_fruit)
#Wylosowany owoc: cherry


random_number = random.randint(1, 6)

print("Wylosowana liczba od 1 do 6:", random_number)
#Wylosowana liczba od 1 do 6: 5


deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(deck)

print("Potasowana talia:", deck)
#Potasowana talia: ['9', '2', 'K', '4', '6', '10', '5', '7', 'A', 'J', '8', 'Q', '3']

numbers = list(range(1, 101))  # Lista liczb od 1 do 100
sampled_numbers = random.sample(numbers, 5)  # Losujemy 5 unikalnych liczb

print("Wylosowane liczby:", sampled_numbers)
#Wylosowane liczby: [75, 4, 61, 26, 1]

andom_float = random.uniform(1.5, 10.5)

print("Wylosowana liczba zmiennoprzecinkowa:", random_float)
#Wylosowana liczba zmiennoprzecinkowa: 7.213211832762841

random_number = random.randrange(0, 100, 5)  # Losuje liczbę co 5, od 0 do 99

print("Wylosowana liczba:", random_number)
#Wylosowana liczba: 35

letters = ['a', 'b', 'c', 'd', 'e']
random_choices = random.choices(letters, k=3)  # Losujemy 3 elementy z powtórzeniami

print("Wylosowane litery:", random_choices)
#Wylosowane litery: ['c', 'd', 'd']

alpha = 2
beta = 5
random_betavariate = random.betavariate(alpha, beta)

print("Losowa liczba z rozkładu Beta:", random_betavariate)
#Losowa liczba z rozkładu Beta: 0.5102341954161893

items = [{"name": "apple", "price": 1}, {"name": "banana", "price": 0.5}, {"name": "cherry", "price": 1.2}]
random.shuffle(items)

print("Potasowane owoce:", items)
#Potasowane owoce: [{'name': 'banana', 'price': 0.5}, {'name': 'apple', 'price': 1}, {'name': 'cherry', 'price': 1.2}]
