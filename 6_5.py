# Schrijf functie gemiddelde(), die de gebruiker vraagt om een willekeurige zin in te voeren.
# De functie geeft vervolgens de gemiddelde lengte van de woorden in de zin als returnwaarde terug.
# Test je code door de methode aan te roepen en het resultaat te printen.

ingevoerde_zin = input('Geef eens een zin: ')


def gemiddelde(zin):
    woorden = zin.split(' ')

    totaal_letters = 0
    for woord in woorden:
        totaal_letters = totaal_letters + len(woord)

    return totaal_letters / len(woorden)


print(gemiddelde(ingevoerde_zin))
