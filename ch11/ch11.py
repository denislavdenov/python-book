#!/usr/bin/env python3

vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)


vowels1 = {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}

print(vowels1)
print(vowels == vowels1)

print(set([2, 3, 2, 5, 5, 4, 3, 1, 2, 1]))

print(set(vowels1))

print(set(range(5)))

vowels1.add('y')
print(vowels1)
vowels1.remove('a')
print(vowels1)
vowels1.clear()
print(vowels1)

ten = set(range(10))
print(ten)
lows = {0, 1, 2, 3, 4}
print(lows)
odds = {1, 3, 5, 7, 9}
lows.add(9)
print(lows)
print(lows.difference(odds))
print(lows.intersection(odds))
print(lows.issubset(ten))
print(lows.issuperset(odds))
lows.remove(0)
print(lows.symmetric_difference(odds))
print(lows.union(odds))

print(lows - odds)
print(lows & odds)
print(lows <= ten)
print(lows >= odds)
print(lows | odds)
print(lows ^ odds)
print()
print()








