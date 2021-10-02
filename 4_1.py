# Schrijf een programma dat de gebruiker vraagt om de score van een multiplechoice toets.
# Het programma bepaalt of het resultaat voldoende is. Bij meer dan 15 punten is de deelnemer geslaagd!
#
# Voorbeelduitvoer:
#
# Geef je score: 18
# Gefeliciteerd!
# Met een score van 18 ben je geslaagd!

score_als_tekst = input('Geef je score: ')
score = int(score_als_tekst)

if score > 15:
    print('1: ', 'Gefeliciteerd!')
    print('1: ', 'Met een score van 18 ben je geslaagd!!')

# Waarschijnlijk heb je de bovenstaande uitvoer geprogrammeerd met 2 print()-opdrachten.
# Wat gebeurt er als je de tweede print()-opdracht niet recht onder de eerste zou plaatsen
# maar bijvoorbeeld recht onder de ‘i’ van het if-statement?

if score > 15:
    print('2: ', 'Gefeliciteerd!')
print('2: ', 'Met een score van 18 ben je geslaagd!!') # dan zie je deze regel dus altijd