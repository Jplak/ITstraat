#Roulette
#Saldo: De speler begint met 10 chips.
#Inzet: De speler kiest hoeveel chips hij wil inzetten.
#Getal: De speler kiest een getal tussen 0 en 36 om op in te zetten.
#Draai: Het roulettewiel draait en kiest een willekeurig getal tussen 0 en 36.
#Winst: Als het getal van de speler overeenkomt met het gedraaide getal, wint de speler 35 keer zijn inzet.
#Doorgaan: De speler kan kiezen om door te gaan of te stoppen.


#eerste poging
import random

def roulette():
    #startsaldo van de speler.
    saldo = 10

    #hoeveelheid chips in bezit.
    print("Welkom bij roulette,")
    print(f"U heeft momenteel {saldo} chips.")

    while saldo > 0:
        #speler kiest inzet
        while True:
            inzet = int(input("Hoeveel chips wilt u inzetten?"))
            if inzet > saldo or inzet <= 0:
                print(f"Je kunt minimaal 1 chip inzetten en maximaal {saldo}.")
            else:
                break
        print(f"U heeft {inzet} chips ingezet.")

        #speler kiest een getal
        while True:
            gekozen_getal = int(input("Kies een getal tussen de 0 en 36: "))
            if 0 <= gekozen_getal <= 36:
                break
            else:
                print("Kies een getal tussen de 1 en 36.")

        #spin spin spin!
        gedraaid_getal = random.randint(0,36)
        print("Het wiel draait...")
        print(f"Het nummer is gevallen op {gedraaid_getal}!")

        #uitkomst roulette ronde
        if gekozen_getal == gedraaid_getal:
            winst = inzet * 35
            saldo += winst
            print(f"Gefeliciteerd! U heeft gewonnen en ontvangt {winst} chips!")
        else:
            saldo -= inzet
            print(f"Ah, jammer! Het getal was {gedraaid_getal}. U heeft niet gewonnen. ")

        #huidig saldo
        print(f"Je hebt momenteel {saldo} chips.")

        #wilt de speler nog een ronde spelen?
        if saldo > 0:
            nog_een_ronde = input("Wilt u doorgaan met spelen, typ dan 'ja' of 'nee'.")
            if nog_een_ronde == "nee":
                print("U heeft gekozen om te stoppen. Het programma eindigt nu.")
                break
        else:
            print("U heeft geen saldo meer, Game over!")
            break

#start het spel opnieuw
roulette()






