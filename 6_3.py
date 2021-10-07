# Schrijf een programma waarmee je het bestand 'pe_6_2_kaartnummers.txt', opnieuw opent en
# het aantal regels,
# het grootste kaartnummer en
# de regel waarop dit grootste kaartnummer in het bestand staat, bepaalt.
#
# Print deze gegevens vervolgens uit:
#
# Deze file telt 6 regels
# Het grootste kaartnummer is: 645345 en dat staat op regel 4
kaartnummers_file = open('6_2_kaartnummers.txt', 'r')
kaartnummers_regels = kaartnummers_file.readlines()

grootste_kaartnummer = -1  # -1 is gewoon een dummy waarde
regelnummer_grootste_kaartnummer = -1
for ix in range(len(kaartnummers_regels)):
    nummer_naam = kaartnummers_regels[ix].split(',')
    # strip haalt eventuele spaties, witregels en andere rommel weg
    nummer = int(nummer_naam[0].strip())  # hier is dit eigenlijk niet nodig
    naam = nummer_naam[1].strip()  # maar hier wel

    if nummer > grootste_kaartnummer:
        grootste_kaartnummer = nummer
        regelnummer_grootste_kaartnummer = ix + 1  # ix start op 0, dat noemen wij mensen de eerste regel

print(f'Deze file telt {len(kaartnummers_regels)}')
print(f'Het grootste kaarnummer is: {grootste_kaartnummer} en dat staat op regel {regelnummer_grootste_kaartnummer}')
kaartnummers_file.close()
