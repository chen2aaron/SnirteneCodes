#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-10
# Blog: morningchen.com


def repeator(n):
    while True:
        n = (yield n)

r = repeator(4)
print r.next()
print r.next()
s = repeator(5)
s.next()
print s.send(None)  # send()方法必须在生成器运行后并挂起才能使用，也就是yield至少被执行一次
