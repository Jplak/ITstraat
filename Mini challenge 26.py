def bubblesort(arr):
    n = len(arr)  # Lengte van de lijst
    for i in range(n):  # Herhaal n keer
        for j in range(0, n - i - 1):  # Laatste i elementen zijn al op hun plaats
            if arr[j] > arr[j + 1]:  # Vergelijk het huidige element met het volgende
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Wissel als het huidige element groter is
    return arr

# Voorbeeldgebruik
lijst = [5, 3, 8, 6, 2]
gesorteerde_lijst = bubblesort(lijst)
print(gesorteerde_lijst)