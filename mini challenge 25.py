def quicksort(arr):
    # Basisgeval: als de lijst 0 of 1 elementen bevat, is deze al gesorteerd
    if len(arr) <= 1:
        return arr

    # Kies een pivot (bijvoorbeeld het laatste element)
    pivot = arr[-1]

    # Verdeel de lijst in twee sublijsten
    smaller = [x for x in arr[:-1] if x <= pivot]  # Elementen kleiner dan of gelijk aan pivot
    greater = [x for x in arr[:-1] if x > pivot]  # Elementen groter dan pivot

    # Recursief sorteer de sublijsten en combineer ze met de pivot
    return quicksort(smaller) + [pivot] + quicksort(greater)


# Voorbeeldgebruik
lijst = [8, 3, 1, 7, 0, 10, 2]
gesorteerde_lijst = quicksort(lijst)
print(gesorteerde_lijst)