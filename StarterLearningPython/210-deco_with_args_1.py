#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-8
# Blog: morningchen.com


def b(fn):
    return lambda s: '<b>%s</b>' % fn(s)


def em(fn):
    return lambda s: '<em>%s</em>' % fn(s)


@b
@em
def greet(name):
    return 'Hello, %s!' % name

print(greet('world'))
