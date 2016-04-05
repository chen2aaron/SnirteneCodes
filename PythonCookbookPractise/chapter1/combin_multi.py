# 1.20. Combining Multiple Mappings into a Single Mapping
from collections import ChainMap


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

# 返回第一次出现的key
merged = ChainMap(a, b)

print(list(merged.items()))

# 动态更新
a['x'] = 42
print(list(merged.items()))
