#!/usr/bin/env python3

# Math expressions
print('Math expressions')
x = 15 - 3
print(x)
x = 15 + 3
print(x)
x = 4 * 7 
print(x)
x = 5 / 2
print(x)
x = 4 / 2
print(x)

# Different types
print('Different types')
x = 15.0 - 11.0
print(x)
x = 19 - 11.0
print(x)

x = 19 - 1.
print(x)
x = 16. - 11
print(x)

# intereger division
print('Integer division')
x = 53 // 24
print(x)

x = 17 // 10
print(x)

x = -17 // 10
print(x)

x = 17 / 10
print(x)

x = -17 / 10
print(x)

# Modulo operator
print('Modulo operator')
x = 53 % 24
print(x)

x = -17 % 10
print(x)

x = 17 % -10
print(x)

x = 20 % 10
print(x)

x = 29 % 10
print(x)

x = 28.5 % 10
print(x)

# Other
print('Other')

x = 2 ** 8
print(x)

x = 2 ** 6
print(x)

x = 2 / 3
print(x)

x = 5 / 3
print(x)

# Operator  Precedence
print('Operator  Precedence')

x = 212 - 32 * 5 / 9
print(x)

x = (212  -  32)  *  5  /  9
print(x)

degrees_celsius  =  26.0
print(degrees_celsius)

x = 9  /  5  *  degrees_celsius  +  32
print(x)

x = degrees_celsius / degrees_celsius
print(x)

# Augmented  Assignment
print('Augmented  Assignment')

score = 50
print(score)
score = score + 20
print(score)

score = 50
print(score)
score += 20
print(score)

d = 2
d *= 3 + 4
print(d)

# Cookie problem
print('Cookie problem')

room_t_c = 20
cooking_t_f = 350
oven_heating_rate_c = 20
oven_heating_time = (((cooking_t_f - 32) * 5 / 9) - room_t_c) / oven_heating_rate_c
print(oven_heating_time)

room_t_c = 20
cooking_t_f = 350
cooking_t_c = (cooking_t_f - 32) * 5 / 9
oven_heating_rate_c = 20
oven_heating_time = (cooking_t_c - room_t_c) / oven_heating_rate_c
print(oven_heating_time)


a = 9 - 3
print(a)
b = 8 * 2.5
print(b)
c = 9 / 2
print(c)
d = 9 / -2
print(d)
e = 9 // -2
print(e)
f = 9 % 2
print(f)
g = 9.0 % 2
print(g)
h = 9 % 2.0
print(h)
i = 9 % -2
print(i)
j = -9 % 2
print(j)
k = 9 / -2.0
print(k)
l = 4 + 3 * 5
print(l)
m = (4 + 3) * 5
print(m)

temp = 24
temp = temp * 1.8 + 32
print(temp)