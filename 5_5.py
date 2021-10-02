# Schrijf (en test) de functie kwadraten_som() die 1 parameter heeft: grondgetallen.
# Dit is een list is met integers.
# De return-waarde van de functie is de som van de kwadraten van alle positieve getallen in de lijst!
# Een lijst van [4, 3, -5 ] heeft als return-waarde dus 25 (namelijk 16 + 9, want -5 is geen positief getal).

def kwadraten_som(grondgetallen):
    totaal = 0
    for getal in grondgetallen:
        if getal >= 0:
            totaal = totaal + getal ** 2

    return totaal


print(kwadraten_som([4, 3, -5]))
