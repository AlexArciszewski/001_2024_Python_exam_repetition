# Zad. 7
# Pamiętasz zadanie nr 9 z cyklu zadań: 5 Podstawy Pętle (to o astronautach)?
# Masz następujące zadanie - zrefaktoryzować wówczas napisany kod w taki sposób, aby rozwiązanie oprzeć o funkcje!

# Zadeklaruj trzy zmienne - pierwszą przechowującą informację o startowym poziomie paliwa, drugą określającą ilość
# astronautów na pokładzie, a trzecią mówiącą, na jakiej wysokości znajduje się rakieta.
#
# 1.	Poproś użytkownika o podanie początkowego poziomu paliwa. Użytkownik ma kontynuować czynność, dopóki nie poda
# poprawnej wartości - mieszczącej się pomiędzy 5000 a 30000 litrów.
# 2.	Stwórz drugą pętlę, która będzie prosić o użytkownika o podanie odpowiedniej ilości astronautów znajdujących
# na pokładzie. Pętla ma walidować podaną liczbę - tak, aby była dodatnia i nie większa niż 7.
# 3.	Zasymuluj pętlą nr 3 lot statku kosmicznego. Kolejne iteracje mają zmniejszać obecny poziom paliwa o określoną
# wartość. Zużycie paliwa co 100 km zależy od ilości astronautów na pokładzie i jest równe: 300 l + 100 * ilosc_astronautow.
#
# Pętla więc ma uruchamiać się co 100 km i wykonać tyle iteracji, na ile wystarczy paliwa. Co każdą iterację ma
# wyświetlać się aktualnie przebyty dystans przez statek kosmiczny.
# 4.4.	Po wykonaniu się pętli, powinien wyświetlić się komunikat: “Statek kosmiczny dotarł do orbity”, jeżeli przebyta
# odległość jest większa niż 2000 km lub w przypadku mniejszej odległości - “Statek kosmiczny nie dotarł do orbity”.


def input_fuel():
    """Function that collects amount of fuel gathered from user"""

    fuel_amount = 0
    while fuel_amount == 0 or fuel_amount not in range(5000, 30001):
        fuel_amount = int(input('Please give me the fuel level: '))
    return fuel_amount


def input_astronauts():
    """Function used for getting the number of astronauts from user """

    astro_team: int = 0
    while astro_team == 0 or astro_team not in range(1, 7):
        astro_team = int(input("Pls give me the number of astronauts: "))
    return astro_team


def fuel_usage_rounded(fuel_amount:int, astro_team: int):
    """Function used to calculate total range of the spaceship and the fuel multiplier fuel usage"""
    hundred_km = 300 + 100 * astro_team
    total_usage = fuel_amount / hundred_km
    total_usage_rounded = round(total_usage)
    return total_usage_rounded


def total_range(total_usage_rounded):
    """Function used to calculate total range of the ship """
    for i in range(0, total_usage_rounded, 1):
        j = i*100
        print("we flew", j, "km")
    if j > 2000:
        print("We are orbiting")


if __name__ == "__main__":
    # input_fuel()
    # input_astronauts()
    # fuel_usage_rounded(input_fuel(), input_astronauts())
    total_range(fuel_usage_rounded(input_fuel(), input_astronauts()))






