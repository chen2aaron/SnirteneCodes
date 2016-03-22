# 1.18. Mapping Names to Sequence Elements
from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('chen2aaron@gmail.com', '2016-3-22')
print(sub)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'date': '2016-3-22'}
dict_to_stock(b)
print(stock_prototype)