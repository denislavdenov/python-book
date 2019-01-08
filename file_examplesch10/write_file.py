#!/usr/bin/env python3

with open('topics.txt', 'w') as output_file: 
    output_file.write('Computer Science')


with open('topics.txt', 'a') as output_file: 
    output_file.write('\nSoftware Engineering')


from typing import TextIO 
from io import StringIO
def sum_number_pairs(input_file: TextIO, output_file: TextIO) -> None:
    for number_pair in input_file:
        number_pair = number_pair.strip()
        operands = number_pair.split()
        total = float(operands[0]) + float(operands[1]) 
        new_line = '{0} {1}\n'.format(number_pair, total) 
        output_file.write(new_line)
if __name__ == '__main__':
    with open('number_pairs.txt', 'r') as input_file, \
            open('number_pair_sums.txt', 'w') as output_file: 
        sum_number_pairs(input_file, output_file)


input_string = '1.5 3.4\n2 4.4\n-1 3\n'
infile = StringIO(input_string)
print(infile.readline())
print(infile.readline())
print(infile.readline())


outfile = StringIO()
outfile.write('1.3 3.4 4.7\n')
outfile.write('2 4.2 6.2\n')
outfile.write('-1 1 0.0\n')

print(outfile.getvalue())





def skip_header(reader: TextIO) -> str:
    # Read the description line
    line = reader.readline()
    # Find the first non-comment line
    line = reader.readline() 
    while line.startswith('#'):
        line = reader.readline()
    # Now line contains the first real piece of data
    return line


def process_file(reader: TextIO) -> None:
    # Find and print the first piece of data
    line = skip_header(reader).strip() 
    print(line)
    # Read the rest of the data
    for line in reader: 
        line = line.strip() 
        print(line)




if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        process_file(input_file)



def smallest_value(reader: TextIO) -> int:
    line = skip_header(reader).strip()
    # Now line contains the first data value; this is also the smallest value # found so far, because it is the only one we have seen.
    smallest = int(line)
    for line in reader:
        value = int(line.strip())
        # If we find a smaller value, remember it.
        if value < smallest: 
            smallest = value
    return smallest

print()

if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        print(smallest_value(input_file))





def find_largest(line: str) -> int:
    largest = -1
    for value in line.split():
        # Remove the trailing period.
        v = int(value[:-1])
        # If we find a larger value, remember it. 
        if v > largest:
            largest = v 
            
    return largest


def process_file(reader: TextIO) -> int:
    line = skip_header(reader).strip()
    largest = find_largest(line)
    for line in reader:
        large = find_largest(line) 
        if large > largest:
            largest = large 
            return largest

if __name__ == '__main__':
    with open('lynx.txt', 'r') as input_file:
        print(process_file(input_file))



def read_molecule(reader: TextIO) -> list:
    line = reader.readline() 
    if not line:
        return None
    parts = line.split()
    name = parts[1]
    molecule = [name]
    reading = True
    while reading:
        line = reader.readline() 
        if line.startswith('END'):
            reading = False 
        else:
            parts = line.split()
            molecule.append(parts[2:])
    return molecule


def read_all_molecules(reader: TextIO) -> list:
    result = []
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:
            result.append(molecule)
        else:
            reading = False
    return result


if __name__ == '__main__':
    molecule_file = open('multimol.pdb', 'r') 
    molecules = read_all_molecules(molecule_file) 
    molecule_file.close()
    print(molecules)


def read_all_molecules1(reader: TextIO) -> list: 
    result = []
    line = reader.readline() 
    while line:
        molecule, line = read_molecule1(reader, line)
        result.append(molecule)
    return result

def read_molecule1(reader: TextIO, line: str) -> list:
    fields = line.split()
    molecule = [fields[1]]
    line = reader.readline()
    while line and not line.startswith('COMPND'):
        fields = line.split() 
        if fields[0] == 'ATOM':
            key, num, atom_type, x, y, z = fields
            molecule.append([atom_type, x, y, z])
        line = reader.readline()
    return molecule, line  

print()

if __name__ == '__main__':
    molecule_file = open('multimol1.pdb', 'r') 
    molecules = read_all_molecules1(molecule_file) 
    molecule_file.close()
    print(molecules)