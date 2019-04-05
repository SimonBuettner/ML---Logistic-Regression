
counter = 0
summe = 0

while True:

    inputGrad = input("Nächste Grad-Zahl (Ende mit q)")

    if inputGrad == "q":
        durchschnitt = float(summe/counter)
        print("Durchschnitt = %.2f" %durchschnitt)
        break

    counter += 1
    summe = float(inputGrad) + summe

