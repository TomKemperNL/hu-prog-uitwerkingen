# De Hogeschool Utrecht wil studenten financieel ondersteunen bij hun studie,
# afhankelijk van de cijfers die een student haalt. Voor elk cijferpunt krijg je € 30,-.
# Voor een 1,0 krijg je dus 30 euro, voor een 2,5 krijg je 75 euro
# en voor een 10,0 beloont de HU een student met € 300,-.
#
# Maak variabelen cijferPROJA, cijferPROG en cijferMOD.
# Geef ze alle drie de waarde die jij verwacht dat je voor de betreffende vakken in blok 1 zult gaan halen.
# Maak nu vervolgens ook de volgende variabelen aan, en bereken de bijbehorende waarden m.b.v. een Python expressie:

cijferPROJA = 6
cijferPROG = 7
cijferMOD = 8
cijfers = [cijferPROJA, cijferPROG, cijferMOD]

# gemiddelde	het gemiddelde van de variabelen cijferPROJA, cijferPROG en cijferMOD.
gemiddelde = sum(cijfers) / len(cijfers)

# beloning	de totale beloning voor deze drie cursussen.
beloning = (cijferPROJA * 30) + (cijferPROG * 30) + (cijferMOD * 30)
print('beloning: ', beloning)

# of algemener

beloning = 0
for cijfer in cijfers:
    beloning = beloning + (cijfer * 30)
print('beloning: ', beloning)

# overzicht
# een string met een tekstuele omschrijving het gemiddelde en de beloning:
#
# Bijvoorbeeld: 'Mijn cijfers (gemiddeld een 7.5) leveren een beloning van € 675.0 op!'

print('Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van € ' + str(beloning) + ' op!')
