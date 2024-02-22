
#Zad 7
# Utwórz w programie zmienne przechowujące Twój wzrost oraz wiek.
# Zapytaj użytkownika o jego wagę i wzrost. Następnie na podstawie tych informacji oblicz
# wartość BMI i umieść ją w zmiennej o etykiecie bmi. Wyświetl wartość obliczonego BMI.
# Wzór na BMI: bmi = waga / wzrost^2 (wzrost ^2 to proces potęgowania)

height = float(input("What's your height [m]? "))
weight = float(input("Whats your weight?  [kg]"))

bmi = weight/height**2
print(f" your bmi is: {bmi}")
