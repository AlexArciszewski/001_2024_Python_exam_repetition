# Zad 5.
# Prześlij przy użyciu **kwargs listę liczb parzystych i nieparzystych. W funkcji dokonaj ich połączenia w jedną
# listę w następujący sposób: [nieparzysta, parzysta nieparzysta, parzysta ...]

all_numbers = []
even_numbers = []
odd_numbers = []
for number in range(31):
    all_numbers.append(number)
    if number % 2 == 0:
        even_numbers.append(number)
    elif number % 2 != 0:
        odd_numbers.append(number)
print(all_numbers)
print(even_numbers)
print(odd_numbers)


def even_and_odd(**kwargs):
    # print("Connecting lists....")

    for key in kwargs:
        print(f"{key}: {kwargs[key]}")
        return (f"{key}: {kwargs[key]}")
even_and_odd(even_numbers=even_numbers)
even_and_odd(odd_numbers=odd_numbers)


