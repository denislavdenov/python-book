#!/usr/bin/env python3

print(str.capitalize('browning'))
print(str.center('Sonnet 43', 36,'.'))
print(str.count('How do I love thee? Let me count the ways. Damn this the', 'the'))

print('someone'.capitalize())
print(('Sonnet 43').center(20))
print('How do I love thee? Let me count the ways.'.count('the'))
print('species'.startswith('a'))
print('species'.startswith('sp'))
print('"{0}" is derived from "{1}"'.format('none', 'no one'))
print('"{0}" is derived from the {1} "{2}"'.format('Etymology', 'Greek', 'ethos'))

my_pi = 3.141591243123


print('Pi rounded to {0} decimal places is {1:.2f}.'.format(2, my_pi))
print('Pi rounded to {0} decimal places is {1:.4f}.'.format(2, my_pi))
print('Pi rounded to {0} decimal places is {1:.6f}.'.format(2, my_pi))
print('Computer Science'.swapcase().endswith('ENCE'))


print('tomato'.count('o'))