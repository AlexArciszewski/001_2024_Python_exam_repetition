# Wyznacz medianę wydatków do pierwszej niedzieli (włącznie) każdego miesiąca (np. dla 2023-09 i 2023-10 są to dni 1, 2, 3 wrz i 1 paź).
#
# Należy zastosować rozwiązanie zgodnie z poniższym pseudokodem.

expenses = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
};
#
# func solution(expenses) {
#     result = null;
#     // ...
#     return result;
# }
# println(solution(expenses));

# Uwagi
#
#     Należy użyć tylko funkcji/modułów ze standardowej biblioteki (np. math).
#     Po przesłaniu poprawnego wyniku:
#         przesłany plik jest finalnym rozwiązaniem
#         uruchomione zostaną testy automatyczne (na różnych danych) badające zużycie pamięci i procesora dla funkcji solution
#     Zadanie może zostać wykonane w języku Python lub JavaScript.
#     Wynik to jedna liczba dla danych spełniających kryteria lub null.


print(expenses)

# Dni do pierwszych niedziel w miesiącu:
# styczeń 01.01 to niedziela więc biore tylko ten dzień ze słownika
#  marzec to 04.03 to sobota bo 07.03 jest już po niedzieli


import math
import datetime

expenses = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
};


def solution(expenses):
    cleared_expenses = {}
    costs = []
    for year_month, month_data in expenses.items():
        for day, day_data in month_data.items():
            for category, values in day_data.items():
                for value in values:
                    day_of_month = int(day)
                    year, month = map(int, year_month.split("-"))
                    date_obj = datetime.datetime(year, month, day_of_month)
                    first_day_of_month = date_obj.replace(day=1)
                    first_sunday_of_month = first_day_of_month + datetime.timedelta(
                        days=((7 - first_day_of_month.weekday()) % 7))
                    if date_obj <= first_sunday_of_month:
                        print(f"{year_month}-{day_of_month} is before or on the first Sunday of the month")
                        cleared_expenses.update({f"{year_month}-{day_of_month}": {f"{category}": f"{values}"}})



                    # elif date_obj >= first_sunday_of_month:
                    #     print(f"{year_month}-{day_of_month} is after the first Sunday of the month")



    #                 for category, values in month_data.items():
    #                     if date_obj <= first_sunday_of_month:
    #                         cleared_expenses.update({f"{year_month}-{day_of_month}": {f"{category}" :f"{values}"}})
    # print(cleared_expenses)
    # for key in cleared_expenses:
    #     print(cleared_expenses[key])
    #     cleared_expenses_by_date = cleared_expenses[key]
    #     for key2 in cleared_expenses:
    #         print(cleared_expenses[key2])


solution(expenses)


# def solution(expenses):
#     cleared_expenses = {}
#     costs = []
#     for year_month, month_data in expenses.items():
#         for day, day_data in month_data.items():
#             for category, values in day_data.items():
#                 for value in values:
#                     day_of_month = int(day)
#                     year, month = map(int, year_month.split("-"))
#                     date_obj = datetime.datetime(year, month, day_of_month)
#                     first_day_of_month = date_obj.replace(day=1)
#                     first_sunday_of_month = first_day_of_month + datetime.timedelta(
#                         days=((7 - first_day_of_month.weekday()) % 7))
#                     if date_obj <= first_sunday_of_month:
#                         print(f"{year_month}-{day_of_month} is before or on the first Sunday of the month")
#
#
#
#                     elif date_obj >= first_sunday_of_month:
#                         print(f"{year_month}-{day_of_month} is after the first Sunday of the month")