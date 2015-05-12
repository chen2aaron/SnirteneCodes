#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-9
# Blog: morningchen.com


class Spring(object):

    """docstring for Spring"""
    __slots__ = ('tree', 'flower')


print dir(Spring)
print Spring.__slots__

s = Spring()
print s.__slots__
Spring.lang = "python"
print Spring.lang
# s.lang = "ruby" # 前面已经通过类给这个属性赋值了。不能用实例属性来修改
print s.lang  # 可以通过实例属性访问
s.tree = "lishu"
print s.tree  # 对于没有通过类属性赋值的 可以用实例属性赋值
print Spring.tree  # 实例属性的值并没有传回到类属性，可以理解为新建立了一个同名的实例属性
Spring.tree = "shushu"  # 再给类属性赋值
print Spring.tree
print s.tree  # 得到结果 类属性与实例属性结果一样
