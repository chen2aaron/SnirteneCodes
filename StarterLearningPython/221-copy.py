#!/usr/bin/env python
# coding=utf-8


import copy


class Mycopy(object):

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


foo = Mycopy(8)

a = ["foo", foo]
b = a[:]
c = list(a)
d = copy.copy(a)
e = copy.deepcopy(a)

a.append("abc")
foo.value = 17

print "original: %r\n slice: %r\n list(): %r\n copy(): %r\n deepcopy(): %r\n" % (a, b, c, d, e)
