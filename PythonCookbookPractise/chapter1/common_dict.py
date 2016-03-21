# 1.9. Finding Commonalities in Two Dictionaries


a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# keys items 并、交、差运算 实际上就是 set集合运算
print(a.keys() | b.keys())
print(set(a.values()) & set(b.values()))  # values 转化成set之后才能进行运算操作
print(a.items() | b.items())
print(a.keys() & b.keys())
print(a.items() & b.items())
print(a.keys() - b.keys())
print(a.items() - b.items())
print('-' * 30)

# filter dict
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)