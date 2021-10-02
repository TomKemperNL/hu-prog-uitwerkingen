# Pas de uitwerking van Practice Exercise 4_2 aan en geef ook een melding als de gebruiker niet mag stemmen!
leeftijd = int(input('Geef je leeftijd: '))
nederlands_paspoort = input('Nederlands paspoort: ') in ['ja', 'Ja', 'yes', 'Yes', 'Yup', 'Zeker weten!']  # etc. etc.

if leeftijd >= 18 and nederlands_paspoort:
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Helaas, je mag niet stemmen...')
