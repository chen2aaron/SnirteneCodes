import sys

s = '{name} has {n} messages.'
s.format(name='uni', n=29)
name = 'uni'
n = 29
print(vars())
print(s.format_map(vars()))


class Info(object):

    def __init__(self, name, n):
        self.name = name
        self.n = n


class SafeDict(dict):

    def __missing__(self, key):
        return '{' + key + '}'


a = Info('uni', 29)
print(vars(a))
print(s.format_map(vars(a)))


def sub(text):
    return text.format_map(SafeDict(sys._getframe(1).f_locals))


print(sub('Hello {name}'))
print(sub('Your favorite color is {color}'))
