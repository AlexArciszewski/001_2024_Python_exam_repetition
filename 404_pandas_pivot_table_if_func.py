#Zadanie 4. Zbuduj tabelę *pivot table* taką jak powyżej w zadaniu 3, ale zamiast wypisanych średnich wzrostów chcemy
# dostać napis "Wysoka osoba" jeśli osoba ma 185 cm wzrostu lub więcej oraz "Zwykła osoba"
# jeśli ma mniej niż 185 cm wzrostu.
#(WSKAZÓWKA: Zbuduj funkcję i zastosuj ją dla obiektu *groupby*)

import pandas as pd


df = pd.read_excel(r"C:\Users\arcis\PycharmProjects\pythonProject25\370_zawody.xlsx")

#Nazwa DataFrame, na podstawie którego chcemy stworzyć tabelę przestawną,
#• Index=’ ‘ -> jaka zmienna ma być naszym indeksem (nazwami wierszy)
#• Columns = ‘ ‘ -> jaka zmienna ma być nazwami kolumn
#• Values = ‘ ‘ -> wartości jakiej zmiennej mają być w środku tabeli przestawnej
#• Aggfunc = ‘ ‘ -> co chcemy obliczyć dla tych wartości (średnią, wartość minimalną itp.)


print('\n')


#pivottable

x = pd.pivot_table(df,
                   index='Płeć',
                   columns='Miasto',
                   values='Wzrost',
                   aggfunc='mean')

print(x)


#Miasto     Gdańsk  Kraków  Warszawa
#Płeć
#Kobieta       NaN   186.5    184.75
#Mężczyzna   185.0   178.0    188.00


def kcalculator(height):
    if height >= 185:
        return 'Wysoka osoba'
    else:
        return 'Niska osoba'

x = df.groupby(['Płeć', 'Miasto']).agg({'Wzrost': 'mean'})
x=x['Wzrost'].apply(kcalculator)
print(x.unstack())

#Miasto           Gdańsk        Kraków      Warszawa
#Płeć
#Kobieta             NaN  Wysoka osoba   Niska osoba
#Mężczyzna  Wysoka osoba   Niska osoba  Wysoka osoba