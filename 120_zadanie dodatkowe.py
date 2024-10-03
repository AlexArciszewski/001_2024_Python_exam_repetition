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


# print(expenses)

# Załozenia:
# Dni do pierwszych niedziel w miesiącu:
# styczeń 01.01 to niedziela więc tylko ten dzień ze słownika
#  marzec to 04.03 to sobota bo 07.03 jest już po niedzieli
#  mediana zliczana z miesiaca wiec spradziczmiany dla dodania dnia dla marca.

from datetime import datetime, timedelta

import statistics
import time



def solution(expenses):
    """Function calculates the expenses from the start of the month up to and including the first Sunday.
    The function returns date and the median of these expenses, or None if there are no expenses"""

    sum_values_list = []
    result = {}
    for year_month, days in expenses.items():
        year, month = map(int, year_month.split("-"))
        # print(year, month)
        first_day = datetime(year, month, 1)
        first_sunday = first_day + timedelta(days=6 - first_day.weekday())
        # print(first_day)
        values = []
        for day, expenses_day in days.items():
            day = int(day)
            if datetime(year, month, day) <= first_sunday:
                food_and_fuel = expenses_day.get("food", []) + expenses_day.get("fuel", [])
                # print(food_and_fuel)
                values.extend(food_and_fuel)
                # print(values)
                for costs in values:
                    # print(costs)
                    sum_values_list.append(costs)
    # print(sum_values_list)
    median = statistics.median(sum_values_list)
    print(median)
    return median



solution(expenses)

