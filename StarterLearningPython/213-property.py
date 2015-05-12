#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-9
# Blog: morningchen.com


class Rect(object):
    """the width and length of rectangle"""
    def __init__(self):
        self.width = 0
        self.length = 0

    def setSize(self, size):
        self.width, self.length = size

    def getSize(self):
        return self.width, self.length

    size = property(getSize, setSize)


if __name__ == '__main__':
    r = Rect()
    r.width = 3
    r.length = 4
    print r.size
    r.size = 30, 100
    print r.width
    print r.length
    print r.size
    r.haha = 3
    print r.haha
