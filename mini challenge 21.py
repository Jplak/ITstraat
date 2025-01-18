# Rekenmachine script

print("Welkom bij de rekenmachine!")
print("Typ een getal, kies een actie (+, -, /, *, =) en blijf doorgaan tot je het resultaat wilt zien.")

# Start met een getal
resultaat = float(input("Voer een getal in: "))

while True:
    # Vraag om de gewenste actie
    actie = input("Welke actie wil je uitvoeren? (+, -, /, *, =): ").strip()

    if actie == "=":
        # Toon het resultaat en stop de rekenmachine
        print(f"Het resultaat is: {resultaat}")
        break
    elif actie in ["+", "-", "/", "*"]:
        # Vraag om een nieuw getal
        nieuw_getal = float(input("Voer een nieuw getal in: "))

        # Voer de gekozen actie uit
        if actie == "+":
            resultaat += nieuw_getal
        elif actie == "-":
            resultaat -= nieuw_getal
        elif actie == "*":
            resultaat *= nieuw_getal
        elif actie == "/":
            if nieuw_getal != 0:
                resultaat /= nieuw_getal
            else:
                print("Fout: Delen door nul is niet toegestaan.")
    else:
        # Ongeldige actie
        print("Ongeldige actie! Kies een van de volgende: +, -, /, *, =.")
