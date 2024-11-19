while True:
    liczba = int(input("Podaj liczbę całkowitą: "))
    if liczba < 0:
        print("Liczba ujemna, wychodzę z pętli")
        break
    print(f"Wprowadzone liczba to: {liczba}")