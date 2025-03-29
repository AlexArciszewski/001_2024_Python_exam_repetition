import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


df =pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx')


print(df.head())
df['Data'] = pd.to_datetime(df['Data'])
print(df.info())
#przypisanie dnaych
x=df['Data']
y=df['Wynik finansowy']
#wykresy i ich opis
#skrocony zapis zamiast poniższego
#plt.plot(x,y, marker='o', linestyle='--', color='b', label='Wynik finansowy')   #można użyć hex string za kolor kolor linestyle marker skracamy
plt.plot(x,y, 'b--o', label='Wynik finansowy') 
plt.plot(x, df['Przychody'],marker='x', color='r', label='Przychody')
#markery->, _ o x + - X D - 


#opisy osi
plt.xlabel('Data')
plt.ylabel('Wynik finansowy')
#tytuł wykresu
plt.title('Wynik finansowy organizacji')
#legenda
plt.legend(loc=2)
plt.show()
#'b'	niebieski (blue)
#'g'	zielony (green)
#'r'	czerwony (red)
#'c'	cyjan (cyan)
#'m'	magenta
#'y'	żółty (yellow)
#'k'	czarny (black)
#'w'	biały (white)
#'.'	kropka
#','	piksel
#'o'	kółko
#'v'	trójkąt w dół
#'^'	trójkąt w górę
#'s'	kwadrat
#'p'	pięciokąt
#'*'	gwiazdka
#'x'	krzyżyk
#'+'	plus
#'D'	romb