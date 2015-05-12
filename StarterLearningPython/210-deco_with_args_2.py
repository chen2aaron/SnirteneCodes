#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-8
# Blog: morningchen.com


def tag_wrap(tag):
    def decorator(fn):
        def inner(s):
            return '<%s>%s<%s>' % (tag, fn(s), tag)
        return inner
    return decorator


@tag_wrap('b')
@tag_wrap('em')
def greet(name):
    return 'Hello, %s!' % name

print(greet('world'))
