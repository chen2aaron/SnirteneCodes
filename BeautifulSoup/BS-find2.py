#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-21
# Blog: morningchen.com
from bs4 import BeautifulSoup
from bs4 import NavigableString
with open("alice.html", "r") as html_doc:
    soup = BeautifulSoup(html_doc.read())


def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))
for tag in soup.find_all(surrounded_by_strings):
    print tag.name
