#!/usr/bin/env python3


velocities = [0.0, 9.81, 19.62, 29.43]
for velocity in velocities:
    print('Metric:', velocity, 'm/sec;', 'Imperial:', velocity * 3.28, 'ft/sec;')

speed = 2
speeds = [1.0, 99.81, 199.62, 299.43]
for speed in speeds:
    print('Metric:', speed, 'm/sec;', 'Imperial:', speed * 3.28, 'ft/sec;')

print('Final value of speed var:', speed)

country = 'United States of America' 
for ch in country:
    if ch.isupper():
        print(ch)


for num in range(10):
    print(num)

print(list(range(10)))
print(list(range(1, 5)))
print(list(range(1, 7)))
print(list(range(0, 8)))

print(list(range(2000, 2050, 4)))


total = 0 
for i in range(1, 101):
    total = total + i 

print(total)

values = [4, 10, 3, 8, -6]

for i in range(len(values)):
    print(i)

for i in range(len(values)):
    print(i, values[i])

for i in range(len(values)):
    values[i] = values[i] * 2
print(values)

metals = ['Li', 'Na', 'K']
weights = [6.941, 22.98976928, 39.0983]

for i in range(len(metals)):
    print(metals[i], weights[i])

outer = ['Li', 'Na', 'K']
inner = ['F', 'Cl', 'Br']

for metal in outer:
    for halogen in inner:
        print(metal + halogen)



def print_table(n: int) -> None:
     # The numbers to include in the table.
    numbers = list(range(1, n + 1))
  
    # Print the header row.
    for i in numbers:
        print('\t' + str(i), end='')
    # End the header row.
    print()
    print()
    # Print each row number and the contents of each row.
    for i in numbers:
        print (i, end='') 
        for j in numbers:
            print('\t' + str(i * j), end='') 
        # End the current row.
        print()
    print()

print(print_table(8))

elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]

for inner_list in elements:
    print(inner_list)

for inner_list in elements:
    for item in inner_list:
        print(item)


info = [['Isaac Newton', 1643, 1727],
        ['Charles Darwin', 1809, 1882],
        ['Alan Turing', 1912, 1954, 'alan@bletchley.uk']]

for item in info:
    print(len(item))


drinking_times_by_day = [["9:02", "10:17", "13:52", "18:23", "21:31"],
                        ["8:45", "12:44", "14:52", "22:17"], 
                        ["8:55", "11:11", "12:34", "13:46","15:52", "17:08", "21:15"], 
                        ["9:15", "11:44", "16:28"],
                        ["10:01", "13:33", "16:45", "19:00"],
                        ["9:34", "11:16", "15:52", "20:37"],
                        ["9:01", "12:24", "18:51", "23:13"]]

for day in drinking_times_by_day:
    for drinking_time in day:
        print(drinking_time, end=' ')
    print()

rabbits = 3
while rabbits > 0:
     print(rabbits)
     rabbits = rabbits - 1


time = 0
population = 1000 # 1000 bacteria to start with 
growth_rate = 0.21 # 21% growth per minute

while population < 2000:
    population = population + growth_rate * population
    print(round(population))
    time = time + 1

print("It took", time, "minutes for the bacteria to double.") 
print("The final population was", round(population), "bacteria.")


text = ""
while text != "quit":
    text = input("Please enter a chemical formula (or 'quit' to exit): ") 
    if text == "quit":
        print("...exiting program") 
        break
    elif text == "H2O":
        print("Water") 
    elif text == "NH3":
        print("Ammonia") 
    elif text == "CH4":
        print("Methane") 
    else:
        print("Unknown compound")


s = 'C3H7'
digit_index = -1 # This will be -1 until we find a digit.
for i in range(len(s)):
    # If we haven't found a digit, and s[i] is a digit
    if digit_index == -1 and s[i].isdigit():
        digit_index = i
        break
print(digit_index)

total = 0 # The sum of the digits seen so far. 
count = 0 # The number of digits seen so far. 
for i in range(len(s)):
    if s[i].isalpha():
        continue
    total = total + int(s[i])
    count = count + 1

print(total,count)