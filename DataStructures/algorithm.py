from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l += [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 =Timer('test1', 'from __main__ import test1')
print('concat:       ', t1.timeit(number=10000000), 'milliseconds')

t2 =Timer('test2', 'from __main__ import test2')
print('append:       ', t2.timeit(number=10000000), 'milliseconds')

t3 =Timer('test3', 'from __main__ import test3')
print('comprehension:', t3.timeit(number=10000000), 'milliseconds')

t4 =Timer('test4', 'from __main__ import test4')
print('list range:   ', t4.timeit(number=10000000), 'milliseconds')

x = list(range(2000000))
pop_front = Timer("x.pop(0)", "from __main__ import x")
print("pop_front     ", pop_front.timeit(number=1000), "milliseconds")
y = list(range(2000000))
pop_end = Timer("y.pop()", "from __main__ import y")
print("pop_end       ", pop_end.timeit(number=1000), "milliseconds")

m = list(range(2000000))
insert_front = Timer("m.insert(0, 100)", "from __main__ import m")
print("insert_front  ", insert_front.timeit(number=1000))
n = list(range(2000000))
insert_end = Timer("n.append(100)", "from __main__ import n")
print("insert_end    ", insert_end.timeit(number=1000))

import timeit
import random

for i in range(10000, 1000001, 20000):
    m = list(range(i))
    n = {j: None for j in range(i)}
    t1 = timeit.Timer("random.randrange(%d) in m" % i, "from __main__ import random, m")
    t2 = timeit.Timer("random.randrange(%d) in n" % i, "from __main__ import random, n")

    lst_time = t1.timeit(number=1000)
    d_time = t2.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
