# Napisz skrypt, który wygeneruje i wyprintuje słownik zawierający liczby pomiędzy
# (1 - n; n jest liczbą podawaną przez użytkownika) w formie (x, x*x).
# Przykładowy input: n = 5
# Oczekiwany wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def main() -> None:
    "Function that creates the dict"
    num = int(input("pls give me the number: "))
    num_list = []
    squared_num = []
    for i in range(1, num + 1):
        num_list.append(i)
        squared_num.append(i**2)
    score_dict = dict(zip(num_list, squared_num))
    print(score_dict)


if __name__ == "__main__":
    main()