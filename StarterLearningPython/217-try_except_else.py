#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-10
# Blog: morningchen.com


while 1:
    try:
        x = raw_input("the first num:")
        y = raw_input("the second num:")
        r = float(x)/float(y)
        print r

    except Exception, e:
        print e
        print "try again."
    else:
        break
