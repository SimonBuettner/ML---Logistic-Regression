import PraxisProjekt_Exception
import PraxisProjekt_Funktionen


erlaubt = {'+', '-', '*', '/'}

while True:

    zeichen = input("+, -, *, /, quit: ")

    if zeichen == "quit":
        break

    elif zeichen not in erlaubt:
        print("Eingabefehler!")
        continue

    else:

        try:
            zahl1 = int(input("Zahl 1 eingeben: "))

        except ValueError as errorM2:
            print("Bitte korrekten Wert für zahl1 eingeben! ", errorM2)
            continue

        else:

            try:
                zahl2 = int(input("Zahl 2 eingeben: "))

            except ValueError as errorM:
                print("Bitte korrekten Wert für zahl2 eingeben! ", errorM)
                continue

            if zeichen == "+":
                    print("Ergebnis: ", PraxisProjekt_Funktionen.addieren(zahl1, zahl2))
            elif zeichen == "-":
                    print("Ergebnis: ", PraxisProjekt_Funktionen.subtrahieren(zahl1, zahl2))
            elif zeichen == "*":
                    print("Ergebnis: ", PraxisProjekt_Funktionen.multiplizieren(zahl1, zahl2))
            else:
                    print("Ergebnis: ", PraxisProjekt_Funktionen.dividieren(zahl1, zahl2))