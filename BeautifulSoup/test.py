#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-22
# Blog: morningchen.com
from bs4 import BeautifulSoup
import urllib

page = "http://movie.douban.com/top250?start=0&filter=&type="
douban_html = urllib.urlopen(page).read()
soup = BeautifulSoup(douban_html)



