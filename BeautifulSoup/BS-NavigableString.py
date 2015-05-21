#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-21
# Blog: morningchen.com
from bs4 import BeautifulSoup
from bs4 import CData
from bs4 import NavigableString


markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string

print type(comment)
print soup
# Comment 对象是一个特殊类型的 NavigableString 对象
print comment
print soup.b.prettify()
print "-" * 50
"""
    Beautiful Soup中定义的其它类型都可能会出现在XML的文档中:
    CData , ProcessingInstruction , Declaration , Doctype .
    与 Comment 对象类似,这些类都是 NavigableString 的子类,
    只是添加了一些额外的方法的字符串独享.下面是用CDATA来替代注释的例子
"""
cdata = CData("A CDATA block")
comment.replace_with(cdata)
print soup.b.prettify()


