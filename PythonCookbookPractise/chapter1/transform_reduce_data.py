# 1.19. Transforming and Reducing Data at the Same Time
import os


nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

files = os.listdir()
print(files)
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

item = ('ACME', 50, 123.45)
print(','.join(str(x) for x in item))

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares_a = min(s['shares'] for s in portfolio)
min_shares_b = min(portfolio, key=lambda s: s['shares'])
