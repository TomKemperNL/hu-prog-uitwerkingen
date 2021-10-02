# Schrijf een functie convert() waar je een temperatuur in graden Celsius
# (als parameter van deze functie) kunt omzetten naar graden Fahrenheit.
# Je kunt de temperatuur in Fahrenheit berekenen met de formule T°F = T°C × 1.8 + 32. Dus 25 °C = 25 × 1.8 + 32 = 77 °F.
#
# Schrijf nu ook een tweede functie table() waarin je met een for-loop van -30 °C t/m 40 °C in stappen van 10 graden
# de temperatuur in Fahrenheit in een string plaatst.
#
# Zorg middels een geformatteerde output voor dezelfde precisie en uitlijning als het voorbeeld hieronder.
# Return de string als resultaat van methode table().
# Test je code door de methode aan te roepen en het resultaat te printen.

def convert(graden_celsius):
    return (graden_celsius * 1.8) + 32


print(f'25C = {convert(25):.0f}F')


def table():
    resultaat = f'{"F":^7} {"C":^7}\n'
    for celsius in range(-30, 41, 10):
        fahrenheit = convert(celsius)
        resultaat = resultaat + f'{fahrenheit:>7.1f} {celsius:>7.1f}\n'

    return resultaat


print(table())
