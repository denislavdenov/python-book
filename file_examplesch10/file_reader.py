#!/usr/bin/env python3

file = open('file_example.txt', 'r') 
contents = file.read()
file.close()
print(contents)

with open('file_example.txt', 'r') as file:
    contents = file.read() 
print(contents)

import os

print(os.getcwd())
os.chdir('/Users/denov/Downloads/python-book/')
print(os.getcwd())
os.chdir('/Users/denov/Downloads/python-book/file_examplesch10')
print(os.getcwd())


with open('file_example.txt', 'r') as example_file: 
    first_ten_chars = example_file.read(18) 
    the_rest = example_file.read()
print("The first 10 characters:", first_ten_chars) 
print()
print("The rest of the file:", the_rest)


with open('file_example.txt', 'r') as example_file: 
    lines = example_file.readlines()
print(lines)


with open('planets.txt', 'r') as planets_file:
    planets = planets_file.readlines()

print(planets)

for planet in reversed(planets):
    print(planet.strip())

print()

for planet in sorted(planets):
    print(planet.strip())


print()

with open('planets.txt', 'r') as data_file:
    for line in data_file:
        print(len(line))




with open('hopedale.txt', 'r') as hopedale_file: 
    # Read and skip the description line.
    hopedale_file.readline()
    # Keep reading and skipping comment lines until we read the first piece 
    # of data.
    data = hopedale_file.readline().strip()
    while data.startswith('#'):
        data = hopedale_file.readline().strip()
    # Now we have the first piece of data. Accumulate the total number of 
    # pelts.
    total_pelts = int(data)
    # Read the rest of the data.
    for data in hopedale_file:
        total_pelts = total_pelts + int(data.strip())
print("Total number of pelts:", total_pelts)





with open('hopedale.txt', 'r') as hopedale_file: 
    # Read and skip the description line.
    hopedale_file.readline()
    # Keep reading and skipping comment lines until we read the first piece 
    # of data.
    data = hopedale_file.readline().rstrip()
    while data.startswith('#'):
        data = hopedale_file.readline().rstrip()
    # Now we have the first piece of data. Accumulate the total number of 
    # pelts.
    print(data)
    # Read the rest of the data.
    for data in hopedale_file:
        print(data.rstrip())







