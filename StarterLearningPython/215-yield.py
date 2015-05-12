#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-7
# Blog: morningchen.com


def g():
    yield 0
    yield 1
    yield 2
    yield 3

print g
print g()
ge = g()
print ge
print type(g) ,type(g()),type(ge)
print dir(ge)
print ge.send()
