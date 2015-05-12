#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-7
# Blog: morningchen.com


def foo(num, str):
    name = "snirtene"
    print locals()
    # print globals()
foo(233, 'your mom boom')


def foos(k, v):
    alais = "xixijun"
    print globals()
foos('xiaobai', 'balalala~')


# print dir(foo)
# print dir(foos)
# {'__builtins__': <module '__builtin__' (built-in)>,
# '__file__': '/Users/chan/MyCodes/StarterLearningPython/test.py',
# '__package__': None,
# '__name__': '__main__',
# 'foo': <function foo at 0x1094145f0>,
# '__doc__': None,
# 'foos': <function foos at 0x109414668>}
