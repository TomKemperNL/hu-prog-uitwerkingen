# Het bestand 'pe_6_2_kaartnummers.txt', bevat klantenkaartnummers en namen

# Schrijf een Python functie pretty_print()waarmee je het bestand opent,
# één string maakt zoals in het voorbeeld hieronder,
# waarbij de informatie per kaart in een nette tekst wordt weergegeven.
#
# Splits hiervoor elke regel op de komma.
#
# Return de uiteindelijke string aan het einde van de functie.
# Vergeet niet het bestand te sluiten!

def pretty_print():
    kaartnummers_file = open('6_2_kaartnummers.txt', 'r')
    kaartnummers_regels = kaartnummers_file.readlines()

    resultaat = ''
    for regel in kaartnummers_regels:
        nummer_naam = regel.split(',')
        # strip haalt eventuele spaties, witregels en andere rommel weg
        nummer = nummer_naam[0].strip()  # hier is dit eigenlijk niet nodig
        naam = nummer_naam[1].strip()  # maar hier wel
        resultaat = resultaat + f'{naam} heeft kaartnummer: {nummer}\n'

    kaartnummers_file.close()
    return resultaat  # waarom heet de functie pretty print terwijl deze returnt? Dat is niet logisch...


print(pretty_print())
