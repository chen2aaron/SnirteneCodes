#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-11
# Blog: morningchen.com

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file="226-bookstore.xml")
print tree
root = tree.getroot()
print root.tag
print root.attrib

for child in root:
    print child.tag, child.attrib

print root[0].tag
print root[0].attrib
print root[0].text
print root[0][0].tag
print root[0][0].attrib
print root[0][0].text

for i in root[0]:
    print i.tag, i.attrib
    print i.text

for ele in tree.iter(tag="book"):
    print ele.tag, ele.attrib

for ele in tree.iter(tag="title"):
    print ele.tag, ele.attrib, ele.text

for ele in tree.iter(tag="author"):
    print ele.tag, ele.attrib, ele.text

for ele in tree.iter():
    print ele.tag, ele.attrib, ele.text

for ele in tree.findall("book"):
    title = ele.find("title").text
    author = ele.find("author").text
    price = ele.find('price').text
    lang = ele.find('title').attrib
    print "-"*50
    print "The book name: "+title
    print "Author: "+author
    print "Price: "+price
