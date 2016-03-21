# 1.11. Naming a Slice


items = list(range(8))
a = slice(2, 4)
print(items)
print(items[2:4])
print(items[a])
items[a] = [20, 13]
print(items)

s = 'HelloWorld, Im your seq'
b = slice(2, 100, 2)

for i in s[b]:
    print(i)

print(b.indices(len(s)))
for i in range(*b.indices(len(s))):
    print(s[i])