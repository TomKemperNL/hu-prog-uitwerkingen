# De tuple letters kan in willekeurige volgorde de letters A, B en C bevatten. Bijvoorbeeld:
#
letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')

# Neem deze tuple over, en schrijf code waarmee je een nieuwe lijst maakt met het aantal voorkomens van de letters in
# alfabetische volgorde. Tuple letters bevat 2 keer ‘A’, 3 keer ‘B’ en 4 keer ‘C’.
# De lijst die dit programma maakt (en print) is dan: [2, 3, 4].

resultaat = [letters.count('A'), letters.count('B'), letters.count('C')]
print(resultaat)

# of, iets algemener, maar met stof die je nog niet hebt gehad:
letters_al_gehad = []
voorkomens_per_letter = []

letters = sorted(letters)  # of letters.sort(), kwestie van smaak

for letter in letters:
    if letter not in letters_al_gehad:
        letters_al_gehad.append(letter)
        aantal_voorkomens = letters.count(letter)
        voorkomens_per_letter.append(aantal_voorkomens)

print(voorkomens_per_letter)
