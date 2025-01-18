from collections import Counter

# Verkiezingen script
stemmen = []

print("Welkom bij de verkiezingen!")
print("Typ een naam om een stem uit te brengen. Typ 'UITSLAG!' om de stemming te beëindigen.")

while True:
    naam = input("Op wie wil je stemmen? ").strip().lower()
    if naam.upper() == "UITSLAG!":
        break
    stemmen.append(naam)

# Tel de stemmen
stem_teller = Counter(stemmen)

if stem_teller:
    # Bepaal de winnaar
    winnaar = stem_teller.most_common(1)[0][0]  # Alleen de naam van de winnaar
    print(f"De winnaar is: {winnaar}!")
else:
    print("Geen stemmen uitgebracht.")