#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-9
# Blog: morningchen.com
'''找出Fibonacci中大于1000的最小的数'''


class Fibs(object):

    """docstring for Fibs"""

    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

fun = Fibs(10000)
a = list(fun)
for i in a:
    if i > 1000:
        print i
        break


# find(fun)

# print [i for i in list(fun) if i > 1000 break]
