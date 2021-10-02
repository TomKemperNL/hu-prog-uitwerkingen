# Schrijf een for-loop die langs alle letters van een string loopt en de letter uitprint,
# maar alleen als het een klinker is ('aeiou').
#
# Gebruik de volgende string:

s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = 'aeiou'

# maar volgens mij is y ook een klinker
klinkers = klinkers + 'y'

for letter in s:
    if letter in klinkers:
        print(letter)

# of iets duidelijker:

for letter in s:
    if letter in klinkers:
        print(letter, end='')  # end='' zorgt er voor dat alles op 1 regel komt
    elif letter == ' ':
        print(' ', end='')
    else:
        print('.', end='')
