# Schrijf een for-loop die over een lijst met getallen itereert, en alle even getallen print.

# alle getallen van 1 tot (niet met) 234, in stapjes van 5...
getallen = range(1, 234, 5)
# of geef zelf een lijst als [2,3,4,5,6]

for getal in getallen:
    if getal % 2 == 0:
        print(getal)
