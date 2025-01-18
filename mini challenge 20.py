import random

# Definieer de loot niveaus en hun kansen
loot_niveaus = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
kansen = [60, 25, 10, 4, 1]  # Percentages van voorkomen (bij elkaar optellen tot 100)

def loot_drop():
    # Gebruik random.choices om een item op basis van kansen te selecteren
    loot = random.choices(loot_niveaus, kansen)[0]
    return loot

# Simuleer een loot drop
print("Je hebt een lootbox geopend!")
verkregen_loot = loot_drop()
print(f"Gefeliciteerd! Je hebt een {verkregen_loot} item gekregen!")