# Pytanie 22 - co zostanie wydrukowane w wyniku wykonania poniższego kodu?

print(False is False)  #True
print(True is False)    #False
print(False is False is False) #True    # (False is False) and (False is False) -> (True) and (True) -> True
print(1 < 3 == 5)   # (1 < 3) and (3 == 5) -> (True) and (False) -> False


# Wszystkie porównania łańcuchowe w Pythonie traktowane są wg tego samego schematu:
# porównanie rozbijane jest na dwuelementowe podgrupy połączone operatorem 'and'
# Przykładowo, porównanie czteroelementowe zostanie potraktowane następująco:
# A is B == C > D  -> (A is B) and (B == C) and (C > D)
# Analogicznie postępujemy dla pięciu i więcej elementów.