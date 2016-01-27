#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-8
# Blog: morningchen.com

class Me(object):
    def foo(self):
        print("shadoumeiyou")

class StaticMe(object):

    @staticmethod
    def foo():
        print("This is Static method foo().")


class ClassMe(object):

    @classmethod
    def bar(cls):

        print("This is Class method bar().")
        print("bar() is part of class:", cls)


if __name__ == '__main__':
    a = Me()
    a.foo()
    print('-'*10)
    static_foo = StaticMe()
    static_foo.foo()
    StaticMe.foo()
    print("*************")
    class_bar = ClassMe()
    class_bar.bar()
    print("*************")
    ClassMe.bar()
    # print("*************")

