import datetime as dt

now = dt.datetime.now()
print(type(now))
#<class 'datetime.datetime'>
print(now)
#2025-06-05 14:28:43.324050
year = now.year
print(year)
#2025
month = now.month
print(month)
#6
print(type(month))
#<class 'int'>

day_week = now.weekday()
print(day_week)
#3 liczy od 0 nie od 1 wiecz czwartek to 3


date_of_birth = dt.datetime(year=1983, month=7, day=14)
print(date_of_birth)
#1983-07-14 00:00:00

print(type(date_of_birth))
#<class 'datetime.datetime'>