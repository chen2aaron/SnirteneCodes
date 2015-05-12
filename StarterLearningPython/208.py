#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-7
# Blog: morningchen.com


class Person(object):

    """docstring for Person"""

    def __init__(self, name, lang="ruby", website="ruby.org"):
        # super(Person, self).__init__()
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "chen2aaron@gmail.com"

    def getName(self):
        return self.name

    def color(self, color):
        print "%s is %s man." % (self.name, color)

lsh = Person("whitecow")
print "1:", lsh.name, lsh.lang, lsh.website, lsh.email
cc = Person('snirtene', "python", "python.org")
print "2:", cc.name, cc.lang, cc.website, cc.email
print "3:", lsh.getName()
print "4:", lsh.color("white")
