#!/usr/bin/env python3

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]

print(whales)
print(whales[0])
print(whales[2])
print(whales[4])
print(whales[-1])
print(whales[-3])

third = whales[2]
print('Third day:', third)
krypton = ['Krypton', 'Kr', -157.2, -153.4]

print(krypton[1])
print(krypton[2])

print(len(whales))
print(max(whales))
print(sorted(whales))
print(sum(whales))

print(len(krypton))

original = ['H', 'He', 'Li']
final = original + ['Be']
print(final)
print(final * 3)
metals = final * 2
print(metals)
del metals[-1]
print(metals)

celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
print(celegans_phenotypes)
useful_markers = celegans_phenotypes[0:4]
print(useful_markers)

celegans_alias = celegans_phenotypes
celegans_phenotypes[5] = 'Lvl'
print(celegans_phenotypes)
print(celegans_alias)

def remove_last_item(L: list) -> list:
    del L[-1]
    return L


print(remove_last_item(celegans_phenotypes))
print(celegans_phenotypes)



colors = ['red', 'orange', 'green']
print(colors)
colors.extend(['black', 'blue'])
print(colors)
colors.append('purple')
print(colors)
colors.insert(2, 'yellow')
print(colors)
colors.remove('black')
print(colors)

life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
print(life[1])
print(life[1][0])
canada = life[0]
print(canada)
print(canada[0])
canada[1] = 86.5
print(canada)
print(life[0])
