#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-8
# Blog: morningchen.com


def wrap_with_prints(fn):
    # This will only happen when a function decorated
    # with @wrap_with_prints is defined
    print('wrap_with_prints runs only once')

    def wrapped():
        # This will happen each time just before
        # the decorated function is called
        print('About to run %s' % fn.__name__)
        # Here is where the wrapper calls the decorated function
        fn()
        # This will happen each time just after
        # the decorated function is called
        print('Done running %s' % fn.__name__)

    return wrapped


@wrap_with_prints
def func_to_decorate():
    print('Running the function that was decorated.')

func_to_decorate()
wrap_with_prints("")
