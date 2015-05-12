#!/usr/bin/env python
# coding=utf-8


class A(object):
    author = "xixijun"

    def __getattr__(self, name):
        if name != "author":
            return "yep, you use __getattr__."

if __name__ == "__main__":
    a = A()
    print a.author
    print a.lang
