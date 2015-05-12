#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-9
# Blog: morningchen.com


class B(object):
    def __getattribute__(self, name):
        print "you use __getattribute__"
        return object.__getattribute__(self, name)

b = B()
# b.y # 报错 'B' object has no attribute 'y'
b.y = 233
print b.y
