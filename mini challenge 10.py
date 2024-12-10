import random

dice = []
totaal = 0
numroll = int(input("hoeveel dobbelstenen wil je gooien?  "))

for die in range(numroll):
	dice.append(random.randint(1,6))
print(dice)

for die in dice:
	totaal += die
print(f"totaal gegooid: {totaal}")