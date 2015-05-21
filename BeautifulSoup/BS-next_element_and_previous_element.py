#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-21
# Blog: morningchen.com
from bs4 import BeautifulSoup
with open("alice.html", "r") as html_doc:
    soup = BeautifulSoup(html_doc.read())

last_a_tag = soup.find("a", id="link3")
print last_a_tag
print last_a_tag.next_element
print last_a_tag.next_sibling

print last_a_tag.previous_element
print last_a_tag.previous_sibling
print "-"*50
# 注意 elements 是复数
for element in last_a_tag.next_elements:
    print repr(element)
