#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-7
# Blog: morningchen.com
'''
ax²+bx+c=0（a≠0）
'''
import math
a = raw_input('Please input a:')
b = raw_input('Please input b:')
c = raw_input('Please input c:')


a = int(a)
b = int(b)
c = int(c)


def equa(a, b, c):
    if a != 0:
        delta = b**2 - 4 * a * c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / 2 / a
            x2 = (-b - math.sqrt(delta)) / 2 / a
            return x1, x2
        elif delta == 0:
            x = (-b + math.sqrt(delta)) / 2 / a
            return x
        else:
            print '无解～'
    else:
        print '这不是二元一次方程啊～'

if __name__ == "__main__":
    roots = equa(a, b, c)
    if roots:
        print '结果是：', roots
