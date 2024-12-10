#Vraag de gebruiker om een bedrag zonder BTW in te vullen. Bereken het bedrag met BTW (21%) en print deze op scherm.

btw = 1.21
print(type(btw))

geenbtw = float(input("Vul aub de prijs zonder BTW in"))
print(type(geenbtw))

metbtw=(geenbtw)*(btw)
print(type(metbtw))

print(f"prijs inclusief btw is {metbtw}")

