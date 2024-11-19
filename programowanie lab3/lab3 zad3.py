ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

liczba_blokow = 5
liczba_lokali = 10

for ulica in ulice:
    for blok in range(1, liczba_blokow + 1):
        for lokal in range(1, liczba_lokali + 1):
            print(f"{ulica} {blok}/{lokal}")