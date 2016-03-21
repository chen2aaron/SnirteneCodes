# 1.7. Keeping Dictionaries in Order
import json
from collections import OrderedDict


d = OrderedDict()
d['hey'] = 4
d['man'] = 1
d['what'] = 2
d['is'] = 9
d['up'] = 10
print(d)
for k in d:
    print(k, d[k])
print(json.dumps(d))
