#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-10
# Blog: morningchen.com


while 1:
    print "this is a division program."
    c = raw_input("input 'c' continuem, otherwise out:")
    if c == "c":
        a = raw_input("first number:")
        b = raw_input("second number:")
        try:
            print float(a) / float(b)
            print "-------------"
        # except (ZeroDivisionError, ValueError), e:
            # print "The second number can't be zero!"
            # print e
            # print "-------------"
        # except ValueError, e:
            # print "please input number."
            # print "-------------"
        except Exception, e:  # 多个异常解决办法
            print e
    else:
        break
