#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-9
# Blog: morningchen.com


class Autumn(object):

    "this is doc."
    season = "the autunm of class"

a = Autumn()  # 实例化
a.season = "instance season"  # 实例属性赋值
print a.__dict__  # 有值
print a.__dict__['season']  # 通过实例dict调用
print a.season  # 通过实例属性调用
print "--------------"
print Autumn.__dict__
print Autumn.__dict__['season']  # 类dict属性调用
print Autumn.season  # 类属性调用
a.lang = "python"  # 实例属性赋值
print a.lang  # 可以这样赋值
print a.__dict__  # 有键值对
print a.__dict__['lang']  # 通过dict调用
Autumn.flower = "peach"  # 类属性赋值
print "------------"
print Autumn.flower  # 有值
print Autumn.__dict__
print Autumn.__doc__  # 注释存在doc里

'''
结论：不管是实例还是类
都用__dict__来存储属性和方法，
可以笼统地把属性和方法称为成员或者特性，
用一句笼统的话说，就是__dict__存储对象成员'''
