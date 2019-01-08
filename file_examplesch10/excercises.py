#!/usr/bin/env python3


#1

filename = input('Which file would you like to back-up? ') 
new_filename = filename + '.bak'
backup = open(new_filename, 'w')
for line in open(filename): 
    backup.write(line)
backup.close()

#2
alkaline_metals = []
for line in open('alkaline_metals.txt'):
    alkaline_metals.append(line.strip().split(' '))
print(alkaline_metals)