# Vraag het aantal spelers
aantal_spelers = int(input("Hoeveel spelers zijn er? "))

# Initialiseer variabelen om de winnaar bij te houden
hoogste_score = -1
winnaar = ""

# Verzamel de naam en score van elke speler
for i in range(aantal_spelers):
    naam = input(f"Wat is de naam van speler {i + 1}? ")
    score = int(input(f"Wat is de score van {naam}? "))

    # Controleer of deze speler de hoogste score heeft
    if score > hoogste_score:
        hoogste_score = score
        winnaar = naam

# Toon wie de winnaar is
print(f"De winnaar is {winnaar} met een score van {hoogste_score}!")
