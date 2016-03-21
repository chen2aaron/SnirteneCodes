# 1.6. Mapping Keys to Multiple Values in a Dictionary
from collections import defaultdict


# dict append list 保持元素的插入顺序
dl = defaultdict(list)
dl['a'].append(1)
dl['a'].append(2)
dl['b'].append(3)
dl['c'].append(4)
print(dl)

# dict append set 去掉重复元素
ds = defaultdict(set)
ds['a'].add(1)
ds['a'].add(2)
ds['b'].add(3)
ds['c'].add(4)
print(ds)

# dict default
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)

pairs = [('a', 1), ('b', 2), ('c', 3), ('c', 4)]
p = defaultdict(list)
for k, v in pairs:
    p[k].append(v)
print(p)