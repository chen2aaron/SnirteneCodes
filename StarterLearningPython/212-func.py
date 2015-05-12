#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-9
# Blog: morningchen.com


class Spring(object):

    def tree(self, x):
        self.x = x
        return self.x

print Spring.__dict__
print Spring.__dict__['tree']

t = Spring()
print '---------'
print t.__dict__  # 空的
print t.tree("appletree")  # 给实例属性赋值
print t.__dict__  # 有值
