#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-7
# Blog: morningchen.com


class Person(object):

    """docstring for Person"""

    def __init__(self, name):
        self.name = name

    def spk(self):
        print "Hello,You are my lover~"

    def height(self, n):
        self.length = n

    def boom(self, n):
        print "%s's size is %d." % (self.name, n)


class Girl(Person):

    """docstring for Girl"""

    def height(self):
        print "%s's height is:177m." % self.name


if __name__ == '__main__':
    cc = Girl('snirtene')
    cc.height()
    cc.boom(79)
    cc.spk()
