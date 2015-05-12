#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-8
# Blog: morningchen.com


def f(x, y):
    return x + y


print f(2, 3)
g = lambda x, y: x + y
print g(3, 5)
print g("snir", "tene")
print g(["hello", "world"], ["python", "ruby"])
print g(("hello", "world"), ("python", "ruby"))


def printx(x):
    return "type({})={} " .format(x, type(x))


a = repr([1, 2, 3])
print printx(a)
b = [1, 2, 3]
print printx(b)
