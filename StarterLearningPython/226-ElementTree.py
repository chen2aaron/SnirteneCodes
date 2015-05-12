#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-11
# Blog: morningchen.com
import os
import time

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file="226-bookstore.xml")
root = tree.getroot()

# for ele in tree.findall("book"):
#     title = ele.find("title").text
#     author = ele.find("author").text
#     price = ele.find('price').text
#     lang = ele.find('title').attrib
#     print "-" * 50
#     print "The book name: " + title
#     print "Author: " + author
#     print "Price: " + price


path = os.getcwd()
file = path + "/226-bookstore.xml"
print root[1].attrib
# del root[1]  #删除元素
# tree.write(file)  #写入

now_time = time.localtime()
print time.asctime(now_time)

# 改价格 设置跟新时间
# for price in root.iter("price"):
#     new_price = float(price.text)+7
#     price.text = str(new_price)
#     print price.text
#     price.set("update", time.asctime(now_time))

# tree.write(file)

# 增加元素
ET.SubElement(root, "book")
for ele in root:
    print ele.tag, ele.attrib

b2 = root[2]
b2.text = "Python"
tree.write(file)
