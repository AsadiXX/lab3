x = int(input("Podaj liczbę gości: "))
n = int(input("Podaj liczbę zamówionych potraw: "))

cena_potraw = 0
i = 0

while i<n:
    danie = float(input(f"Podaj cenę dania: {i+1}"))
    cena_potraw += danie
    i += 1
if n>0:
    srednia_cena_potrawy = cena_potraw/n
else:
    print("Liczba potraw musi być większa od 0")

if x>0:
    sredni_koszt_goscia = cena_potraw/x
else:
    print("Liczba gosci przy stoliku musi być większa od 0")

print(f"Koszt zamówia każdego gościa wniósł {sredni_koszt_goscia:.2f}")