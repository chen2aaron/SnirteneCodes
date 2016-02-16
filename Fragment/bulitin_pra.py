from collections import namedtuple, deque, OrderedDict
from copy import copy, deepcopy
import itertools

Point = namedtuple('P', ['x', 'y'])
p = Point(1, 4)
print(p.x)
print(p.y)

q = deque(['a', 'b', 'c'])
q.append('x')
print(q)
q.appendleft({'y': 1})
print(q)
q.popleft()
print(q)

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

x = [1, 2, 3, 4, ['a', 'b', 'c']]
y = copy(x)
z = deepcopy(x)
m = x
x[4].append('d')
print(x, id(x))
print(m, id(m))
print(y, id(y))
print(z, id(z))

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for x in itertools.chain(['a', 'b', 'c'], ['x', 'y', 'z']):
    print(x)
for n in ns:
    print(n)

cs = itertools.repeat('A', 20)
for a in cs:
    print(a)

# cx = itertools.cycle([2, 5, 3])
# for c in cx:
#     print(c)
