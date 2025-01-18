from datetime import datetime

# Vraag de geboortedatum van de gebruiker
geboortedatum_str = input("Voer je geboortedatum in (dd-mm-jjjj): ")

# Zet de invoer om naar een datetime-object
geboortedatum = datetime.strptime(geboortedatum_str, "%d-%m-%Y")

# Haal de huidige datum op
huidige_datum = datetime.now()

# Bereken de leeftijd van de gebruiker
leeftijd = huidige_datum.year - geboortedatum.year - ((huidige_datum.month, huidige_datum.day) < (geboortedatum.month, geboortedatum.day))

# Toon of de gebruiker mag motorrijden
if leeftijd >= 18:
    print(f"Je bent {leeftijd} jaar oud en mag motorrijden in Nederland!")
else:
    print(f"Je bent {leeftijd} jaar oud en mag nog niet motorrijden in Nederland.")
