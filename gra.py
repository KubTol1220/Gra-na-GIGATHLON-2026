# main.py
# Rybacy na połów w Gigathlonie

import random

MIN_X = -10
MAX_X = 10
MIN_Y = -10
MAX_Y = 10

while True:

    print("\n RYBACY NA POŁÓW W GIGATHLONIE \n")

    # Nazwa statku
    nazwa = input("Podaj nazwę statku: ")

    # Pozycja X
    try:
        x = int(input("Podaj pozycję startową X (-10 do 10): "))

        if x < MIN_X or x > MAX_X:
            print("❗ X poza zakresem. Ustawiono X = 0")
            x = 0

    except:
        print("❗ Błędna wartość. Ustawiono X = 0")
        x = 0

    # Pozycja Y
    try:
        y = int(input("Podaj pozycję startową Y (-10 do 10): "))

        if y < MIN_Y or y > MAX_Y:
            print("❗ Y poza zakresem. Ustawiono Y = 0")
            y = 0

    except:
        print("❗ Błędna wartość. Ustawiono Y = 0")
        y = 0

    # Paliwo
    try:
        paliwo = int(input("Podaj ilość paliwa (minimum 50): "))

        if paliwo < 50:
            print("❗ Za mało paliwa. Ustawiono 50")
            paliwo = 50

    except:
        print("❗ Błędna wartość. Ustawiono 50")
        paliwo = 50

    # Cel połowu
    try:
        cel = int(input("Ile tuńczyków trzeba złowić? (1-5): "))

        if cel < 1 or cel > 5:
            print("❗ Niepoprawna liczba. Ustawiono 3")
            cel = 3

    except:
        print("❗ Błędna wartość. Ustawiono 3")
        cel = 3

    krok = 0
    tunczyki = 0

    wynik = ""
    powod = ""

    historia = []

    # Elementy świata
    jaskinie = [(-2, 3), (4, -1), (0, 5)]

    porty = [(2, 2), (-4, -3)]

    # Łowiska tuńczyków
    ryby = [(1, 2), (-3, 4), (5, -1), (0, 6), (-5, -5)]

    print("\n--- START WYPRAWY ---")
    print(f"Statek: {nazwa}")
    print(f"Pozycja startowa: ({x}, {y})")
    print(f"Paliwo: {paliwo}")
    print(f"Cel: złowić {cel} tuńczyków")

    print("\nGranice świata: od -10 do 10")

    print("\nZnane łowiska tuńczyków:")
    print(ryby)

    print("\nSterowanie:")
    print("W - góra")
    print("S - dół")
    print("A - lewo")
    print("D - prawo")

    # Główna pętla gry
    while True:

        # Sukces
        if tunczyki >= cel:

            print("\n🏆 SUKCES!")
            print("Złowiono wszystkie wymagane tuńczyki!")

            wynik = "SUKCES"
            powod = "Osiągnięto cel połowu"

            break

        # Brak paliwa
        if paliwo <= 0:

            print("\n❌ PORAŻKA!")
            print("Statek nie ma już paliwa.")

            wynik = "PORAŻKA"
            powod = "Brak paliwa"

            break

        krok += 1

        print(f"\n--- KROK {krok} ---")

        print(f"Pozycja przed ruchem: ({x}, {y})")
        print(f"Paliwo przed ruchem: {paliwo}")
        print(f"Złowione tuńczyki: {tunczyki}/{cel}")

        ruch = input("Ruch (W/A/S/D): ").upper()

        stare_x = x
        stare_y = y

        # Ruch
        if ruch == "W":
            y += 1

        elif ruch == "S":
            y -= 1

        elif ruch == "A":
            x -= 1

        elif ruch == "D":
            x += 1

        else:
            print("❗ Niepoprawny ruch")
            continue

        paliwo -= 5

        print(f"Ruch z ({stare_x}, {stare_y}) -> ({x}, {y})")
        print("Zużyto 5 paliwa")

        # Granice świata
        if x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y:

            print("❌ Wypłynąłeś poza mapę!")

            wynik = "PORAŻKA"
            powod = "Opuszczenie świata"

            break

        # Jaskinie
        if (x, y) in jaskinie:

            print("Trafiłeś na jaskinię!")
            print("Strata 10 paliwa")

            paliwo -= 10

            historia.append("Jaskinia")

        # Porty
        if (x, y) in porty:

            print("Wpłynięto do portu!")
            print("Odzyskano 25 paliwa")

            paliwo += 25

            historia.append("Port")

        # Łowisko ryb
        if (x, y) in ryby:

            print("Znaleziono łowisko tuńczyków!")
            print("Złowiono 1 tuńczyka!")

            tunczyki += 1

            ryby.remove((x, y))

            historia.append("Połów tuńczyka")

        # Losowe zdarzenia
        los = random.randint(1, 100)

        # Piraci 10%
        if los <= 10:

            print("ATAK PIRATÓW!")
            print("Piraci ukradli 5 paliwa!")

            paliwo -= 5

            historia.append("Atak piratów")

        # Sztorm 20%
        elif los <= 30:

            print("SZTORM!")
            print("Strata 10 paliwa")

            paliwo -= 10

            historia.append("Sztorm")

        print(f"Paliwo po ruchu: {paliwo}")

    # Raport końcowy
    print("\n RAPORT KOŃCOWY")
    print(f"Statek: {nazwa}")
    print(f"Końcowa pozycja: ({x}, {y})")
    print(f"Liczba kroków: {krok}")
    print(f"Pozostałe paliwo: {paliwo}")
    print(f"Złowione tuńczyki: {tunczyki}")
    print(f"Wynik wyprawy: {wynik}")
    print(f"Powód zakończenia: {powod}")

    print("\nNajważniejsze zdarzenia:")

    if len(historia) == 0:
        print("Brak zdarzeń")

    else:
        for zdarzenie in historia:
            print("-", zdarzenie)

    # Ponowna gra
    jeszcze = input("\nCzy chcesz zagrać jeszcze raz? (T/N): ").upper()

    if jeszcze != "T":
        print("\nKoniec gry.")
        break
    