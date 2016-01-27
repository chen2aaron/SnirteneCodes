#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-21
# Blog: morningchen.com
from bs4 import BeautifulSoup
with open("alice.html", "r") as html_doc:
    soup = BeautifulSoup(html_doc.read())
    # 按照标准的缩进格式的结构输出 自动补充</body></html>>
print(soup.prettify)

"""
    一个Tag可能包含多个字符串或其它的Tag,
    这些都是这个Tag的子节点.
    Beautiful Soup提供了许多操作和遍历子节点的属性.
    操作文档树最简单的方法就是告诉它你想获取的tag的name.
"""
print "-" * 50
print soup.head
print soup.title
print soup.title.name
print soup.title.parent
print soup.title.parent.name
print soup.p
print soup.p['class']
print soup.b
print soup.a
print soup.find_all('a')
print soup.find(id='link3')
# 从文档中找到所有<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))
# 从文档中获取所有文字内容
print "-"*50
print(soup.body.get_text())

"""
    .contents 和 .children
"""
head_tag = soup.head
print "-" * 50
print head_tag
print head_tag.contents
title_tag = head_tag.contents[0]
print title_tag
print title_tag.contents
print soup.head.contents[0].contents
for child in title_tag.children:
    print child
print list(soup.children)
print "-" * 50
print list(soup.descendants)
print "-" * 50

