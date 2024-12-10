import random

input('Hoeveel spelers zijn er:  ')
players = list(input('Voer de namen van de spelers in met een komma tussen elke naam:  ').split())
eerste =(random.choice(players))
print (f"{eerste} mag als eerst.")