#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-9
# Blog: morningchen.com


class Myrange(object):

    """docstring for Myrange"""

    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


if __name__ == '__main__':
    x = Myrange(9)
    print x.next()
    print x.next()
    print "----------"
    for i in x:
        print i
    # print .next
