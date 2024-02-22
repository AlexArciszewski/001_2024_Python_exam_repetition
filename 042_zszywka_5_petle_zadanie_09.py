# Zad. 9
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



fuel_level = 0
spacemen_onboard = 0
latitude = 0

while fuel_level not in range(5000, 30001):
    fuel_level = int(input('please give me the fuel level: '))
while spacemen_onboard not in range(1, 7):
    spacemen_onboard = int(input('please give me the number of astronauts: '))
hundred_km = 300 + 100 * spacemen_onboard
total_usage = fuel_level/hundred_km
print(total_usage)
total_usage_rounded = round(total_usage)
print(total_usage_rounded)
total_range = total_usage_rounded * 100
print(total_range)
for i in range(0, total_usage_rounded, 1):
    j = i*100
    print("we flew", j, "km")
if j > 2000:
    print("We are orbiting")
else:
    print("We didn't manage to orbiting")
# for i in total_usage_rounded:
#     print(f"We flew{i*100} kilometers")
# if i*100 > 2000:
#     print(f"We left our orbit")

