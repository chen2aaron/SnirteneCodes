# 4.5. Iterating in Reverse


a = [2, 6, 7, 11]
for x in reversed(a):
    print(x)


# Print a file backwards
# 需要预先定义__reversed__() 或者转换成list
# f = open('somefile')
# for line in reversed(list(f)):
#     print(line, end='')


class Countdown(object):
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(30)):
    print(rr)
for rr in Countdown(30):
    print(rr)
