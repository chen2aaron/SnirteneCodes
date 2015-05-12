#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-8
# Blog: morningchen.com


class Serect(object):

    """docstring for Serect"""

    def __init__(self):
        self.me = 'snirtene'
        self.__name = 'xixijun'

    # @property
    def __mylover(self):
        print "I love you~"

    def answer(self):
        print "Who is your lover?"
        self.__mylover()

    @property
    def name(self):
        return self.__name

if __name__ == '__main__':
    p = Serect()
    print p.me
    print p.name  # 不用@property 就只能通过函数（方法）调用 例如p.name()
    p.answer()
    # p.__mylover()
