from datetime import datetime, timedelta
import statistics


def solution(expenses):
    """Function calculates the expenses from the start of the month up to the first Sunday.
    The function returns the median of expenses for all months given"""

    sum_values_list = []
    for year_month, days in expenses.items():
        year, month = map(int, year_month.split("-"))
        first_day = datetime(year, month, 1)
        first_sunday = first_day + timedelta(days=6 - first_day.weekday())
        values = []
        for day, expenses_day in days.items():
            day = int(day)
            if datetime(year, month, day) <= first_sunday:
                food_and_fuel = expenses_day.get("food", []) + expenses_day.get("fuel", [])
                values.extend(food_and_fuel)
                for costs in values:
                    sum_values_list.append(costs)
    median = statistics.median(sum_values_list)
    return median



