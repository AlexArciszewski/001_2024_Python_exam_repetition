
from datetime import datetime, timedelta

import statistics

def solution(expenses):
    """Function calculates the expenses from the start of the month up to and including the first Sunday.
    The function returns date and the median of these expenses, or None if there are no expenses"""

    result = {}
    for year_month, days in expenses.items():
        year, month = map(int, year_month.split("-"))
        first_day = datetime(year, month, 1)
        first_sunday = first_day + timedelta(days=6 - first_day.weekday())
        values = []
        for day, daily_expenses in days.items():
            day = int(day)
            if datetime(year, month, day) <= first_sunday:
                food_and_fuel = daily_expenses.get("food", []) + daily_expenses.get("fuel", [])
                values.extend(food_and_fuel)
        if values:
            median = statistics.median(values)
            result[year_month] = median
        else:
            result[year_month] = None
    return result


solution(expenses)

