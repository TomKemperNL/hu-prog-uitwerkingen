a = 6
b = 7
c = (a + b) / 2

voornaam = "Monty"
tussenvoegsel = "de"
achternaam = "Piton"
mijn_naam = voornaam + ' ' + tussenvoegsel + ' ' + achternaam

# 1. 6.75 groter is dan a en kleiner b.
resultaat = 6.75 > a and 6.75 < b
print('1:', resultaat)
# of korter
resultaat = b > 6.75 > a
print('1:', resultaat)

# 2. de lengte van mijnnaam even groot is als de som van de lengte van voornaam, tussenvoegsel en achternaam.
resultaat = len(mijn_naam) == len(voornaam) + len(tussenvoegsel) + len(achternaam)
print('2:', resultaat)

# 3. de lengte van mijnnaam minstens 5 maal groter is dan variabele c.
resultaat = len(mijn_naam) >= (5 * c)
print('3:', resultaat)

# 4. de waarde van variabele tussenvoegsel voorkomt in de waarde van variabele achternaam.
resultaat = tussenvoegsel in achternaam
print('4:', resultaat)