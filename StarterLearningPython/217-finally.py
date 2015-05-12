#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-10
# Blog: morningchen.com

x = 10
try:
    x = 1/0

except Exception, e:
    print e
    print "try again."
finally:
    print "del x"
    del x
# print x
