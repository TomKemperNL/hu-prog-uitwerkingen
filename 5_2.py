# Schrijf (en test) de functie som() die 1 parameter heeft: getallenLijst.
# Ga ervan uit dat dit een list is met integers.
# De return-waarde van de functie moet de som (optelling) van de getallen in de lijst zijn!
# Tip: bekijk nog eens de list-functies (Perkovic, blz. 28).

def som(getallenLijst):
    totaal = 0
    for getal in getallenLijst:
        totaal = totaal + getal
    return totaal


print(som([1, 2, 3]))


# maar, stiekem kan ook, dus zou je nooit die functie maken:

def som(getallenLijst):
    return sum(getallenLijst)


print(som([1, 2, 3]))
