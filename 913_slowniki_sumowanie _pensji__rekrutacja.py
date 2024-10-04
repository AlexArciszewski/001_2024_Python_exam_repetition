# Korzystając ze słownika pensje zawierającego informację o wynagrodzeniach w firmie, wydrukuj sumę pensji
# wszystkich pracowników.

# Sumowanie
pensje = {'ksiegowa': 5000, 'kierowca': 4500, 'recepcjonistka': 4000}

sum_salary = []
for values in pensje.values():
    sum_salary.append(values)

print(sum_salary)

total = sum(sum_salary)
print(total)

print("Opcja B 1 linia kodu")

print(sum(pensje.values()))


