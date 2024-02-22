# Zad 4.
# Wyobraź sobie, że jesteś pogodynką i robisz zestawienie opadów deszczu na dany miesiąc.
# Problem polega jednak na tym, że dane miasta wraz z opadami są nieuporządkowane oraz
# użytkownik może wpisywać nieskończenie wiele par: miasto oraz opad aż do momentu podania
# pustej linii. Twoim zadaniem jest zinterpretowanie podanych danych wejściowych i podać wynik
# na wzór poniższego przykładu.
#
# Wejście:
# Boston 12
# Londyn 10
# Boston 12
# [pusta linia]
#
# Wyjście:
# Boston : 24
# # Londyn : 10
#
temp_results = int(input("How may temperature measurement results U have? "))
var = temp_results
#
#
# cities = []
# temperatures = []
# # city = input("city: ")
# # outside_temp = int(input("outside temp: "))
#
cities = []
temperatures = []
#
while var > 0:

     city = input("city: ")
     cities.append(city)
     outside_temp = input("outside temp: ")
     temperatures.append(outside_temp)
     print(cities, temperatures)
     var = var - 1
     if var == 0:
         break

# cities = ['Boston', 'Londyn', 'Boston', '']
# temperatures = ['12', '10', '12', '']

cities_temps = dict(zip(cities, temperatures))
print(cities_temps)


# for key in cities_temps.copy().keys():
#      if cities_temps.copy().keys() == '' or ' ':
#          cities_temps.pop(key)
# print(cities_temps)

for key, value in list(cities_temps.items()):
    if value == '':
        del cities_temps[key]
print(cities_temps)

# zip_dict = dict(zip(new_dict_keys_list, new_dict_values_list))
# print(zip_dict)



