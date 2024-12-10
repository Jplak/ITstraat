x = input("Voer 5 getallen in met een spatie tussen elk cijfer.")
x= x.strip().split()
x.sort(reverse=True)
print(x)