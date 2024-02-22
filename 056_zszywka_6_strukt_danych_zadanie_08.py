# Zad 7
# Utwórz w programie zmienne przechowujące Twój wzrost oraz wiek.
# Zapytaj użytkownika o jego wagę i wzrost. Następnie na podstawie tych informacji oblicz
# wartość BMI i umieść ją w zmiennej o etykiecie bmi. Wyświetl wartość obliczonego BMI.
# Wzór na BMI: bmi = waga / wzrost^2 (wzrost ^2 to proces potęgowania)

height = float(input("What's your height [m]? "))
weight = float(input("Whats your weight?  [kg] "))

bmi = weight/height**2
print(f" your bmi is: {bmi}")

# Zad 8.
# Pamiętasz program służący do wyliczania BMI? Trochę go ulepszymy. Od teraz program powinien klasyfikować obliczoną
# wartość BMI konkretnej kategorii: niedowaga / waga normalna / lekka nadwaga / nadwaga. Dodatkowo w przypadku
# nadwagi chcemy sprawdzić, czy mamy do czynienia z otyłością.


if bmi < 18.5:
    print("U are to skinny")
elif bmi > 18.5 and bmi < 24:
    print(" U are ok")
elif bmi >= 24 and bmi < 26.5:
    print("U are overweight a bit")
elif bmi > 26.5:
    print("U are overweight ")
elif bmi > 30 and bmi < 35:
    print( "U are obese: I lvl")
elif bmi > 35 and bmi < 40:
    print("U are obese: II lvl")
elif bmi > 40:
    print("U are obese II levl")