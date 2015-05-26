#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-27
# Blog: morningchen.com


from pyquery import PyQuery as pq


def get_img(url):
    """
        class用.commentlist
        img 子类
        tag 用attr
        注意d(item)
    """
    d = pq(url)
    for item in d('.commentlist img'):
        print d(item).attr('src')


if __name__ == '__main__':
    url = "http://jandan.net/pic/page-6614"
    get_img(url)
