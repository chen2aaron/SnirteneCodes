#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-21
# Blog: morningchen.com
from bs4 import BeautifulSoup
with open("alice.html", "r") as html_doc:
    soup = BeautifulSoup(html_doc.read())

"""
    find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.
    如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.
    效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.
    文档树中有3个tag符合搜索条件,但结果只返回了2个,因为我们限制了返回数量
"""
print soup.find_all("a", limit=2)
