#!/usr/bin/env python3

def convert_to_celsius(fahrenheit: float) -> float:

    return (fahrenheit - 32.0) * 5.0 / 9.0

def above_freezing(celsius: float) -> bool:

    return celsius > 0

fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
celsius = convert_to_celsius(fahrenheit)
print(celsius)
if above_freezing(celsius):
    print('It is above freezing.')
else:
    print('It is below freezing.')