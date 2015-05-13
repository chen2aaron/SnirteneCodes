#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-7
# Blog: morningchen.com


def outer_foo():
    a = 10

    def inner_foo():
        global a
        a = 20
        print "inner_foo: a=", a
    # inner_foo()
    print "outer_foo: a=", a

a = 30
outer_foo()
print "a=", a
