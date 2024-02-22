# Zad 4.
# Napisz program wyświetlający nazwę dnia tygodnia zależnie od liczby wprowadzonej przez użytkownika
# (1 – poniedziałek ,…, 7 – niedziela, inna – „nie ma takiego dnia”)

week = {1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday", 7 : "Sunday" }
day_of_the_week = int(input("Please choose the number of the day: "))
for key in week.keys():
    if key == day_of_the_week:
        print(week[key])
