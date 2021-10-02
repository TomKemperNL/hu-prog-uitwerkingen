# Schrijf (en test) de functie lang_genoeg() die voor Efteling-attracties bepaalt of een gebruiker in een attractie mag.
# De functie heeft één parameter, namelijk de lengte van de gebruiker in centimeters.
# Als de gebruiker 120 centimeter of langer is de return-waarde van de functie
# “Je bent lang genoeg voor de attractie!”, anders is de return-waarde
# “Sorry, je bent te klein!”.

def lang_genoeg(lengte_cm):
    if lengte_cm >= 120:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'


print(lang_genoeg(206))

# maar netter is om hier een boolean te returnen en andere code de boodschap te laten bepalen...
