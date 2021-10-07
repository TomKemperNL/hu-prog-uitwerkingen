# Bij een marathonwedstrijd worden bij een controlepost alle voorbijkomende hardlopers genoteerd.
# De gegevens van elke hardloper worden in het bestand pe_6_4_hardlopers.txt opgeslagen.
# Schrijf een programma waarmee een tekstbestand wordt aangemaakt (als het bestand nog niet bestaat)
# of aangevuld (gebruik de append-mode) met de gegevens van één hardloper (inlezen van toetsenbord).
#
# Let op: je zult je programma in deze opdracht steeds opnieuw moeten uitvoeren voor elke nieuwe hardloper.
# Om dit te voorkomen zou je een while-loop kunnen gebruiken, maar die behandelen we pas volgende les.
# Je kunt er natuurlijk voor kiezen om daar alvast naar te kijken (niet verplicht).
#
# Bestand pe_6_4_hardlopers.txt (na registratie van 5 hardlopers):
#
# Thu 10 Mar 2016, 10:45:52, Miranda
# Thu 10 Mar 2016, 10:46:04, Piet
# Thu 10 Mar 2016, 10:47:27, Sacha
# Thu 10 Mar 2016, 10:48:33, Karel
# Thu 10 Mar 2016, 10:48:42, Kemal
# Gebruik de Python-functie strftime() om de huidige tijd in een keurig formaat om te zetten!
# Je kunt de documentatie (Koppelingen naar een externe site.)
# van deze functie bekijken of in het boek van Perkovic (blz. 106-107) lezen
# hoe je onderstaande voorbeeld kunt ombouwen tot de gewenste tijdsaanduiding!
#
# Voorbeeld met functie strftime():
#
# import datetime
# vandaag = datetime.datetime.today()
# s = vandaag.strftime("%a %d %b %Y")
# print(s)
# Uitvoer van bovenstaande code:
#
# Mon 12 Sep 2016
import datetime

hardlopers = open('6_4_hardlopers.txt', 'a')

while True:
    naam = input('Vul de naam in van de hardloper die zojuist is binnengekomen (of q om af te sluiten): ')
    if naam == 'q':
        break
    if naam == '':
        continue  # als je per ongeluk op enter drukt, dan schrijven we geen regel

    nu = datetime.datetime.now()
    nu_als_tekst = nu.strftime('%a %d %b, %H:%M:%S')
    hardlopers.write(f'{nu_als_tekst}, {naam}\n')

    hardlopers.flush()  # dit zorgt er voor dat elke hardloper direct zichtbaar is in het bestand

hardlopers.close()  # anders zie je de nieuwe hardlopers nu pas
