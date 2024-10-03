from datetime import datetime, timedelta


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

}

from datetime import datetime, timedelta

import statistics


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

}
from datetime import datetime, timedelta

import statistics


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

}


result = {}

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

    if values:

        median = statistics.median(values)

        result[year_month] = median

    else:

        result[year_month] = None


print(result)