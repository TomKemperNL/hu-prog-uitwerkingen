# Je mag stemmen als je 18 of ouder bent èn in het bezit bent van een Nederlands paspoort.
#
# Schrijf een programma dat de leeftijd van de gebruiker vraagt en of diegene een Nederlands paspoort heeft (ja/nee).
# Als aan beide voorwaarden is voldaan, print dan dat de gebruiker mag stemmen!
#
# Doe dit weer in een nieuw bestand, bijvoorbeeld pe4_2.py.
# In de conditie van een if-statement kun je meerdere voorwaarden tegelijk controleren met bijvoorbeeld or of
# and (zie Perkovic blz 18 en 19). Voor deze opgave mag je daarom maximaal 1 keer een if-statement gebruiken.
#
# Voorbeelduitvoer:
#
# Geef je leeftijd: 18
# Nederlands paspoort: ja
# Gefeliciteerd, je mag stemmen!

leeftijd = int(input('Geef je leeftijd: '))
nederlands_paspoort_als_tekst = input('Nederlands paspoort: ')
nederlands_paspoort = nederlands_paspoort_als_tekst in ['ja', 'Ja', 'yes', 'Yes', 'Yup', 'Zeker weten!']  # etc. etc.

if leeftijd >= 18 and nederlands_paspoort:
    print('Gefeliciteerd, je mag stemmen!')
