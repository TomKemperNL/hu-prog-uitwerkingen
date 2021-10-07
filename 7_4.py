# Schrijf een programma met twee for-loops in elkaar (nested) om de tafels van 1 t/m 10 uit te printen.

tafels = range(1, 11)
for tafel in tafels:
    for aantal_keer in range(1, 11):
        print(f'{aantal_keer:2} x {tafel:2} = {aantal_keer * tafel:>3}')
