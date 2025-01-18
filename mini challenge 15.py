# Sinterklaas verlanglijst script
verlanglijst = []

print("Welkom bij de Sinterklaas verlanglijst!")
print("Typ één voorwerp dat je wilt en druk op Enter. Typ 'KLAAR!' als je klaar bent.")

while True:
    item = input("Wat wil je graag van Sinterklaas? ")
    if item.upper() == "KLAAR!":
        break
    verlanglijst.append(item)

# Sorteer de lijst alfabetisch
verlanglijst.sort()

# Toon de verlanglijst
print("Je verlanglijst in alfabetische volgorde:")
for item in verlanglijst:
    print(f"- {item}")
