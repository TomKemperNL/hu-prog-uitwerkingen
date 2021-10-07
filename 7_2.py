# Schrijf een functie analyzer() waaraan je een string met variabelen meegeeft, gescheiden door streepjes
# (voorbeeld: "5-9-7-1-7-8-3-2-4-8-7-9").
# Splits deze parameter in een lijst van getallen, en sorteer de lijst van klein naar groot.
# Return daarna als tuple de volgende informatie:
# (<gesorteerde lijst>, <grootste waarde>, <kleinste waarde>, <aantal getallen>, <som van de getallen>, <gemiddelde>)

def analyzer(tekst):
    gesplitst = tekst.split('-')
    getallen = []
    for getal_als_tekst in gesplitst:
        getallen.append(int(getal_als_tekst))

    getallen.sort()
    # alternatief: getallen = sorted(getallen)
    grootste = max(getallen)
    kleinste = min(getallen)
    aantal = len(getallen)
    som = sum(getallen)
    gemiddelde = som / aantal

    return (getallen, grootste, kleinste, aantal, som, gemiddelde)  # Python heeft deze haakjes eigenlijk niet nodig
    # maar aangezien we tuples nog niet zo vaak gezien hebben, zet ik ze er even ter verduidelijking neer


resultaat = analyzer("5-9-7-1-7-8-3-2-4-8-7-9")

# Gesorteerde list van ints: [1, 2, 3, 4, 5, 7, 7, 7, 8, 8, 9, 9]
# Grootste getal: 9 en Kleinste getal: 1
# Aantal getallen: 12 en Som van de getallen: 70
# Gemiddelde: 5.833333333333333

print(f'Gesorteerde list van ints: {resultaat[0]}')
print(f'Grootste getal: {resultaat[1]} en Kleinste getal: {resultaat[2]}')
print(f'Aantal getallen: {resultaat[3]} en Som van de getallen: {resultaat[4]}')
print(f'Gemiddelde: {resultaat[5]}')
