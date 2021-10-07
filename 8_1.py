# Schrijf een while-loop die steeds getallen van de gebruiker vraagt tot deze 0 ingeeft:
#
# Uitvoer:
#
# Geef een getal: 5
# Geef een getal: -1
# Geef een getal: 0
# Er zijn 2 getallen ingevoerd, de som is: 4

getal = int(input('Geef een getal: '))
aantal_getallen = 0
som = 0

while getal != 0:
    aantal_getallen = aantal_getallen + 1
    som = som + getal
    getal = int(input('Geef een getal: '))

print(f'Er zijn {aantal_getallen} ingevoerd, de som is: {som}')
