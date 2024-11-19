paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Pozostało {paliwo} litrów paliwa")
    paliwo -= paliwo_zużyte_na_s
    czas = czas+1
    print(f"Czas lotu: {czas}")
print("koniec lotu")