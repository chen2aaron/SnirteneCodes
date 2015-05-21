#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-21
# Blog: morningchen.com
import re
from bs4 import BeautifulSoup
with open("alice.html", "r") as html_doc:
    soup = BeautifulSoup(html_doc.read())

# 如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容
for tag in soup.find_all(re.compile("^t")):
    print tag.name

# 如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.
# 下面代码找到文档中所有<a>标签和<b>标签:
print soup.find_all(['a', 'b'])

# True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
for tag in soup.find_all(True):
    print tag.name


# 下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True
# 但是返回了包含了id的属性  这是为毛！！！！！跟文档说的不一样啊！！！！！！！
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
print soup.find_all(has_class_but_no_id)
