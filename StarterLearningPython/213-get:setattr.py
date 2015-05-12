#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-9
# Blog: morningchen.com


class A(object):

    """docstring for A"""

    def __getattr__(self, name):
        print "you use __getattr__"
        pass

    def __setattr__(self, name, value):
        print "you use __setattr__"
        self.__dict__[name] = value
a = A()
# A.x  # 不能通过类 访问一个不存在的属性
a.x  # 当发现x不在A里面的时候 调用了getattr
a.x = 233  # 赋值调用了setattr
print a.x
