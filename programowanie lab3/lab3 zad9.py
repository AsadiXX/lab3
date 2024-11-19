imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
wiek = input("Podaj wiek: ")

print(f"Witaj: {imie}")
print(f"Twój wiek to: {wiek}")

print(imie, nazwisko, imie[0],nazwisko[0])

lancuch = input("Podaj łańcuch znaków: ")
print(lancuch * 5)

lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
lancuch3 = lancuch1 + lancuch2
print("Połączone łańcuchy:", lancuch3)

polowa = lancuch3[:len(lancuch3) // 2]
print("Pierwsza połowa połączonych łańcuchów:", polowa)