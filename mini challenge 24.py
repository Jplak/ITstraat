import random


def dobbelsteen_ggooien(invoer):
    # Probeer de invoer in het formaat 'AdX' te splitsen
    try:
        aantal, zijden = invoer.lower().split('d')
        aantal = int(aantal)  # Aantal dobbelstenen
        zijden = int(zijden)  # Aantal zijden per dobbelsteen

        # Controleer of het aantal dobbelstenen en zijden geldig zijn
        if aantal <= 0 or zijden <= 0:
            print("Het aantal dobbelstenen en de zijden moeten groter zijn dan 0.")
            return

        # Gooi de dobbelstenen en bereken de som
        resultaat = sum(random.randint(1, zijden) for _ in range(aantal))
        print(f"Je hebt {aantal} dobbelstenen met {zijde} zijden gegooid. De som is: {resultaat}")
    except ValueError:
        print("Ongeldig formaat. Zorg ervoor dat je de invoer in de vorm 'AdX' geeft, bijvoorbeeld '3d6'.")


def main():
    while True:
        invoer = input("Geef de dobbelstenen op in de 'AdX' notatie (bijv. 3d6): ").strip()
        dobbelsteen_ggooien(invoer)


if __name__ == "__main__":
    main()