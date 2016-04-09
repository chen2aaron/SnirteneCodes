# Combining and Concatenating Strings


parts = ['Is', 'Chicago', 'Not', 'Chicago?']
data = ['ACME', 50, 91.1]
print(' '.join(parts))
print(' '.join(str(d) for d in data))
print('a', 'b', 'c', sep=' ')


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


print(' '.join(sample()))


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ' '.join(parts)
            parts = []
            size = 0
        yield ' '.join(parts)

# 结合文件操作
with open('filename', 'w') as f:
    for part in combine(sample(), 4):
        f.write(part)