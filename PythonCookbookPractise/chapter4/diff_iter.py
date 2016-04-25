# 4.9 - 4.12
from itertools import permutations, combinations, combinations_with_replacement, zip_longest, chain

items = ['a', 'b', 'c']

for p in permutations(items):
    print(p)

print('-' * 30)

for p in permutations(items, 2):
    print(p)

print('-' * 30)

for c in combinations(items, 2):
    print(c)

print('-' * 30)

for c in combinations_with_replacement(items, 3):
    print(c)

print('-' * 30)

data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

for i, (x, y) in enumerate(data):
    print(i, x, y)

print('-' * 30)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
print(list(zip(a, b)))
print(list(zip_longest(a, b, fillvalue='cool')))

print('-' * 30)

# better than a + b
for i in chain(a, b):
    print(i)
