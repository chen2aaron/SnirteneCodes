import re


r = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
a = 'a b     c'
print(r)
print(a.split(' '))
print(re.split(r'\s+', a))