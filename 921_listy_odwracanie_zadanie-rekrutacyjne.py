# Używając dowolnej metody odwróć listę odwroc_mnie i zapisz ją do zmiennej odwrocona.
odwroc_mnie = ['trudne', 'takie', 'bylo', 'nie', 'To']
odwrocona = odwroc_mnie
odwroc_mnie.reverse()

print(odwrocona)

odwroc_mnie = ['trudne', 'takie', 'bylo', 'nie', 'To']
print(odwroc_mnie[::-1])


odwroc_mnie = ['trudne', 'takie', 'bylo', 'nie', 'To']
odwrocona = []
for string in odwroc_mnie:
    odwrocona.insert(0, string)
print(odwrocona)

odwroc_mnie = ['trudne', 'takie', 'bylo', 'nie', 'To']
odwrocona = list(reversed(odwroc_mnie))
print(odwrocona)