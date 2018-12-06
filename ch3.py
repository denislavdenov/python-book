#!/usr/bin/env python3

x = abs(-9)
print(x)

x = abs(3.3)
print(x)

day_t = 3
night_t = 10
x = abs(day_t - night_t)
print(x)

x = abs(-7) + abs(3.3)
print(x)

x = pow(abs(-2), round(4.3))
print(x)

x = pow(abs(-2), round(4.6))
print(x)

x = int(34.6)
print(x)

x = int(34.9)
print(x)

x = int(-4.6)
print(x)

x = float(3)
print(x)

x = round(3.141592653, 5)
print(x)


print(id(-9))

shoe_size = 8.5
print(id(shoe_size))

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print(convert_to_celsius(80))

def quadratic(a, b, c, x):
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third

print(quadratic(2, 3, 4, 0.5))

print(quadratic(1, 1, 1, 1))
print(quadratic(13, 7, 3, 2))


def f(x):
 x=2*x
 return x


x = 2
x = f(x + 1) + f(x + 2)
print(x)

print(min(2, 3, 4))
print(max(2, -3, 4, 7, -5))
print(max(2, -3, min(4, 7), -5))
print(min(max(3, 4), abs(-5)))
print(abs(min(4, 6, max(2, 8))))
print(round(max(5.572, 3.258), abs(-2)))

def f3(x):
 x=x * 3
 return x

def f4(x,y):
    return abs(x-y)

def f5(km):
    return km / 1.6

def f6(x,y,z):
    return (x + y + z) / 3

print(f6(15,30,120))

def f9(x):
    return x ** 2