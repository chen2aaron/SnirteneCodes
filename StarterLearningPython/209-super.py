#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-8
# Blog: morningchen.com


class Person(object):

    """docstring for Person"""

    def __init__(self, name):
        self.name = name

    def whoAreYou(self):
        print "The person's name is {}.".format(self.name)


class Girl(Person):

    """docstring for Girl"""

    def __init__(self, name):
        super(Girl, self).__init__(name)
        # super(Girl, self).whoAreYou()
        gender = 'female'
        print "{}'s gender is {}.".format(self.name, gender)

if __name__ == '__main__':
    A1 = Girl("YangChoujiao")
    A1.whoAreYou()
