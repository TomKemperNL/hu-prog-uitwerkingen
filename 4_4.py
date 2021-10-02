# Schrijf een for-loop die over een lijst met strings itereert, en van elk woord de eerste twee karakters print.
# De lijst [ ‘maandag’, ‘dinsdag’, ‘woensdag’ ] zou dus moeten resulteren in:
#
# ma
# di
# wo

dagen = ['maandag', 'dinsdag', 'woensdag']

for dag in dagen:
    eerste_letter = dag[0]
    tweede_letter = dag[1]
    print(eerste_letter + tweede_letter)
