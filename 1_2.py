# 1. Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious'?

resultaat = len('Supercalifragilisticexpialidocious')
print(resultaat)

# 2. Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor?

resultaat = 'ice' in 'Supercalifragilisticexpialidocious'
print(resultaat)

# 3. Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?
resultaat = len('Antidisestablishmentarianism') > len('Honorificabilitudinitatibus')
print(resultaat)

# 4. Welke componist komt in alfabetische volgorde het eerst: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'?
componisten = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']

# twee mogelijkheden:
# A) Zonder de componisten-lijst aan te passen
resultaat = sorted(componisten)
print(resultaat)  # kijk hier bijv. in de 'Debugger', en zie dat de componistenlijst nog onaangeraakt is

# 5. Welke het laatst in het rijtje van vraag 4?
resultaat = sorted(componisten, reverse=True)
print(resultaat)

# B) Wel de componisten-lijst aan te passen
componisten.sort()
print(componisten)

# 5. Welke het laatst in het rijtje van vraag 4?
componisten.sort(reverse=True)
print(componisten)
