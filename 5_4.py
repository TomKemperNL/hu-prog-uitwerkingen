# Schrijf (en test) een functie new_password() die 2 parameters heeft: oldpassword en newpassword.
# De return-waarde is True als het nieuwe password voldoet aan de eisen.
# Het nieuwe password wordt alleen geaccepteerd als
# het verschilt van het oude password
# èn als het minimaal 6 tekens lang is.
#
# Als dat niet zo is, is de return-waarde False.
#
# Optioneel: zorg dat het nieuwe password minstens 1 cijfer moet bevatten!

def new_password(oldpassword, newpassword):
    lang_genoeg = len(newpassword) >= 6
    anders_dan_oude = not (newpassword == oldpassword)

    heeft_cijfer = False
    for cijfer in '123456789':
        if cijfer in newpassword:
            heeft_cijfer = True

    return lang_genoeg and anders_dan_oude and heeft_cijfer


print(new_password('ditwasnietheelsterk', 'maarditookniet1'))
