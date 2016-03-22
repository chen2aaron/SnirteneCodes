# 1.16. Filtering Sequence Elements
from itertools import compress


mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# list comprehension 占用大量内存
filter_a = [n for n in mylist if n > 0]
clip_neg = [n if n > 0 else 0 for n in mylist]

# generator expressions
filter_b = (n for n in mylist if n > 0)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


# 过滤器函数
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

# Boolean 序列
more5 = [n > 5 for n in counts]
print(list(compress(addresses, more5)))