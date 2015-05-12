# coding: utf8
'''
问题描述

斐波那契数列

by AaronChen
'''
a = 0
b = 1
for i in range(10):
    a, b = b, a + b
print a
