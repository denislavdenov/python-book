#!/usr/bin/env python3

from typing import Set, TextIO 
from io import StringIO

def observe_birds(observations_file: TextIO) -> Set[str]:
    birds_observed = set()
    for line in observations_file:
        bird = line.strip()
        birds_observed.add(bird)
    
    for species in birds_observed:
        print(species)
    return birds_observed

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    with open('observations.txt') as observations_file:
        print(observe_birds(observations_file))


canada = ['Canada', 76.5]
usa = ['United States', 75.5] 
mexico = ['Mexico', 72.0]
print(mexico)
life = (canada, usa ,mexico)

print(life)


mexico = ['Mexico', 82.5]
print(life)
print(mexico)


(x, y) = (10, 20)
print(x)
print(y)

dict1 = {'canada goose': 3, 'northern fulmar': 1}
print(dict1)


print(dict1['canada goose'])

bird_to_observations = {}
bird_to_observations['snow goose'] = 33
bird_to_observations['eagle'] = 999
print(bird_to_observations)
del bird_to_observations['snow goose']
print(bird_to_observations)
print()
bird_to_observations1 = {'canada goose': 183, 'long-tailed jaeger': 71, 'snow goose': 63, 'northern fulmar': 1}
for bird in bird_to_observations1:
    print(bird, bird_to_observations1[bird])


