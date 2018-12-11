#!/usr/bin/env python3

#Not
print(not True)
#And
print(True and True)
print(True and False)
#OR
print(True or False)
print(True or True)
print(False or False)


print(5 > 6)

def is_positive(x):
    return x > 0

print(is_positive(3.5))
print(is_positive(-3.5))

print(not '')
print(not 'bad')

print('A' < 'a')
print('Feb' in '01 Jan 1838')

date = input('Enter a date in the format DD MTH YYYY: ')
print('Jan' in date)


ph = float(input('Enter the pH level: '))
if ph < 7.0:
    print(ph,"is acidic")

if ph > 7.0:
    print(ph,"is basic")


ph = float(input('Enter the pH level: '))
if ph < 7.0:
    print(ph, "is acidic")
elif ph > 7.0:
    print(ph, "is basic")
elif ph == 7.0:
    print(ph, "is neutral")

compound = input('Enter the compound: ')
if compound == "H2O":
    print("Water")
elif compound == "NH3":
    print("Ammonia")
elif compound == "CH4":
    print("Methane")
else:
    print("Unknown compound")


value = input('Enter the pH level: ') 
if  0 < float(value) < 14.1:
    ph = value 
    if ph < 7.0:
        print(ph, "is acidic.") 
    elif ph > 7.0:
        print(ph, "is basic.") 
    else:
        print(ph, "is neutral.") 
else:
    print("No pH value was given!")


