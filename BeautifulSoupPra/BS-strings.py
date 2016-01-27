#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-21
# Blog: morningchen.com
from bs4 import BeautifulSoup
with open("alice.html", "r") as html_doc:
    soup = BeautifulSoup(html_doc.read())
print soup.strings

for string in soup.strings:
    print string
print "*"*50

"""
    输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容
"""
for text in soup.stripped_strings:
    print text
